from django.shortcuts import render, redirect
from django.contrib import messages
from .services.auth_service import authenticate_user
from .repositories.user_repository import user_exists_by_email, get_user_by_email
from .forms import UserInfoForm
from .models import User
import uuid
import random
import re
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings

def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = get_user_by_email(email)
        if not user:
            messages.error(request, '입력한 이메일 주소를 찾을 수 없습니다.')
        elif user.password != password:
            messages.error(request, '비밀번호가 올바르지 않습니다.')
        else:
            request.session['user_id'] = str(user.id)

            return redirect('user:home')

    return render(request, 'user/home_01.html')


def find_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if user_exists_by_email(email):
            request.session['reset_email'] = email
            return redirect('user:find_password_complete')
        else:
            messages.error(request, '입력한 이메일 주소를 찾을 수 없습니다.')
    return render(request, 'user/search_01.html')


def find_password_complete(request):
    email = request.session.get('reset_email')
    user = get_user_by_email(email)
    return render(request, 'user/search_02.html', {'user': user})


def logout_view(request):
    request.session.flush()
    messages.info(request, "로그아웃 되었습니다.")
    return redirect('user:home')

def info(request):
    if request.method == 'POST':
        return redirect('user:info')
    return render(request, 'user/info.html')

def get_or_create_user(request):
    if request.user.is_authenticated:
        return request.user, True
    temp_email = f"guest_{uuid.uuid4().hex[:10]}@example.com"
    user = User.objects.create(email=temp_email, password="guest_password")
    return user, False

def info_submit(request):
    if request.method == "POST":
        user, _ = get_or_create_user(request)

        #  Checkbox 값 'on' → True 처리
        post_data = request.POST.copy()
        post_data['marital_skipped'] = post_data.get('marriage_skip_btn') == 'on'
        post_data['children_skipped'] = post_data.get('children_skip_btn') == 'on'
        post_data['other_skipped'] = post_data.get('other_skip_btn') == 'on'
        post_data['detail_skipped'] = post_data.get('detail_skip_btn') == 'on'

        # 자녀 유무 라디오 버튼 → Boolean 처리
        if 'child_status' in post_data:
            post_data['has_children'] = post_data.get('child_status') == 'yes'

        # 폼 객체 생성
        form = UserInfoForm(post_data)

        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = user
            user_info.save()
            return redirect("user:home")

        # 유효성 실패 시 경고 메시지 팝업으로 표시
        for field, errors in form.errors.items():
            for error in errors:
                messages.warning(request, f"{error}")

        return render(request, "user/info.html", {"form": form})

    # GET 요청 시 빈 폼 렌더링
    return render(request, "user/info.html", {"form": UserInfoForm()})

def info_cancel(request):
    messages.info(request, "입력이 취소되었습니다.")
    return redirect("user:home")

def join_user_form(request):
    return render(request, 'user/join_01.html')


def join_user_email_form(request):
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        email_domain = request.POST.get('email_domain')
        password = request.POST.get('password')
        full_email = f"{email_id}@{email_domain}"

        # 이메일 유효성 검사
        try:
            validate_email(full_email)
        except ValidationError:
            messages.error(request, '유효하지 않은 이메일 형식입니다.')
            return redirect('user:join_01')

        # 이메일 중복 체크
        if User.objects.filter(email=full_email).exists():
            messages.error(request, '이미 등록된 이메일입니다.')
            return redirect('user:join_01')

        # 비밀번호 형식 확인
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d|[^A-Za-z\d])(?=.{8,16}).*$', password):
            messages.error(request, '비밀번호 형식이 올바르지 않습니다.')
            return redirect('user:join_01')

        # 인증코드 생성 후 세션 저장
        auth_code = str(random.randint(10000, 99999))
        request.session['user_email'] = full_email
        request.session['user_password'] = password
        request.session['auth_code'] = auth_code

        # 메일 전송
        subject = "[LawQuick] 이메일 인증번호 안내"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [full_email]
        verification_link = "http://localhost:8080/join/email/certification"

        html_content = render_to_string('email_verification.html', {
            'verification_code': auth_code,
            'verification_link': verification_link
        })

        email = EmailMultiAlternatives(subject, '', from_email, to_email)
        email.attach_alternative(html_content, "text/html")
        email.send()

        return redirect('user:join_03')

    return redirect('user:join_01')


def join_user_email_certification(request):
    if request.method == 'POST':
        user_input = request.POST.get('auth_code')
        session_code = request.session.get('auth_code')
        email = request.session.get('user_email')
        password = request.session.get('user_password')

        # 세션 만료 처리
        if not email or not password or not session_code:
            messages.error(request, '세션이 만료되었습니다. 다시 회원가입을 진행해주세요.')
            return redirect('user:join_01')

        if user_input != session_code:
            return render(request, 'user/join_03.html', {
                'error': '❌ 인증번호가 일치하지 않습니다. 다시 입력해주세요.'
            })

        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'user/join_03.html', {
                'error': '❌ 유효하지 않은 이메일 형식입니다.'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'user/join_03.html', {
                'error': '❌ 이미 등록된 이메일입니다. 로그인 또는 비밀번호 찾기를 이용해주세요.'
            })

        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d|[^A-Za-z\d])(?=.{8,16}).*$', password):
            return render(request, 'user/join_03.html', {
                'error': '❌ 비밀번호는 영문자와 숫자 또는 특수문자를 포함한 8~16자여야 합니다.'
            })

        try:
            hashed_pw = make_password(password)
            print("✅ 사용자 생성 시도 중:", email)

            user = User(email=email, password=hashed_pw, is_verified=True)
            user.save()

            print("✅ 사용자 생성 완료:", user)
        except Exception as e:
            return render(request, 'user/join_03.html', {
                'error': f'❌ 회원가입에 실패했습니다. 관리자에게 문의해주세요. ({str(e)})'
            })

        request.session.flush()
        return redirect('user:join_04')

    # GET 요청으로 들어온 경우
    return render(request, 'user/join_03.html', {
        'error': '❗ 인증 절차를 완료하려면 인증번호를 입력해주세요.'
    })



def join_terms_privacy(request):
    return render(request, 'user/join_p_terms_privacy.html')


def join_terms_service(request):
    return render(request, 'user/join_p_terms_service.html')


def join_user_complete(request):
    return render(request, 'user/join_04.html')