import random
import re
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('user:info')
            else:
                messages.error(request, '비밀번호가 일치하지 않습니다.')
        except User.DoesNotExist:
            messages.error(request, '존재하지 않는 사용자입니다.')

    return render(request, 'user/home_01.html')

def find_password(request):
    if request.method == 'POST':
        return redirect('user:find_password_email_confirm')
    return render(request, 'user/search_01.html')

def find_password_email_confirm(request):
    if request.method == 'POST':
        return redirect('user:find_password_complete')
    return render(request, 'user/search_02.html')

def find_password_complete(request):
    return render(request, 'user/search_03.html')

def join_user_form(request):
    return render(request, 'user/join_01.html')

def join_user_email_form(request):
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        email_domain = request.POST.get('email_domain')
        password = request.POST.get('password')
        full_email = f"{email_id}@{email_domain}"

        # 이메일 형식 검사
        try:
            validate_email(full_email)
        except ValidationError:
            messages.error(request, '유효하지 않은 이메일 형식입니다.')
            return redirect('user:join_01')

        # 이메일 중복 검사
        if User.objects.filter(email=full_email).exists():
            messages.error(request, '이미 등록된 이메일입니다.')
            return redirect('user:join_01')

        # 비밀번호 형식 검사
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d|[^A-Za-z\d])(?=.{8,16}).*$', password):
            messages.error(request, '비밀번호 형식이 올바르지 않습니다.')
            return redirect('user:join_01')

        auth_code = str(random.randint(10000, 99999))
        request.session['user_email'] = full_email
        request.session['user_password'] = password
        request.session['auth_code'] = auth_code

        subject = "[LawQuick] 이메일 인증번호 안내"
        from_email = 'your_email@gmail.com'
        to_email = [full_email]
        verification_link = f"http://localhost:8080/join/email/certification"

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

        if user_input != session_code:
            return render(request, 'user/join_03.html', {
                'error': '인증번호가 일치하지 않습니다. 다시 입력해주세요.'
            })

        # DB 저장 전 중복 검사 및 검증
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        import re
        from django.contrib.auth.hashers import make_password

        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'user/join_03.html', {
                'error': '유효하지 않은 이메일 형식입니다.'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'user/join_03.html', {
                'error': '이미 등록된 이메일입니다.'
            })

        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d|[^A-Za-z\d])(?=.{8,16}).*$', password):
            return render(request, 'user/join_03.html', {
                'error': '비밀번호 형식이 올바르지 않습니다.'
            })

        # 회원 정보 저장 (최종 1회)
        hashed_pw = make_password(password)
        User.objects.create(email=email, password=hashed_pw, is_verified=True)

        return redirect('user:join_04')

    return render(request, 'user/join_03.html')

def join_terms_privacy(request):
    return render(request, 'user/join_p_terms_privacy.html')

def join_terms_service(request):
    return render(request, 'user/join_p_terms_service.html')

def join_user_complete(request):
    return render(request, 'user/join_04.html')

def logout_view(request):
    request.session.flush()
    messages.success(request, '정상적으로 로그아웃되었습니다.')
    return redirect('user:home')
