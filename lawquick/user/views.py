from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserInfoForm
from .models import User
import uuid

def home(request):
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

        # ✅ Checkbox 값 'on' → True 처리
        post_data = request.POST.copy()
        post_data['marital_skipped'] = post_data.get('marriage_skip_btn') == 'on'
        post_data['children_skipped'] = post_data.get('children_skip_btn') == 'on'
        post_data['other_skipped'] = post_data.get('other_skip_btn') == 'on'
        post_data['detail_skipped'] = post_data.get('detail_skip_btn') == 'on'

        # ✅ 자녀 유무 라디오 버튼 → Boolean 처리
        if 'child_status' in post_data:
            post_data['has_children'] = post_data.get('child_status') == 'yes'

        # ✅ 폼 객체 생성
        form = UserInfoForm(post_data)

        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = user
            user_info.save()
            return redirect("user:home")

        # ❗유효성 실패 시 경고 메시지 팝업으로 표시
        for field, errors in form.errors.items():
            for error in errors:
                messages.warning(request, f"{error}")

        return render(request, "user/info.html", {"form": form})

    # GET 요청 시 빈 폼 렌더링
    return render(request, "user/info.html", {"form": UserInfoForm()})

def info_cancel(request):
    messages.info(request, "입력이 취소되었습니다.")
    return redirect("user:home")