from django.shortcuts import render, redirect
from .models import UserInfo, User
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
    # 로그인한 사용자라면 그냥 반환
    if request.user.is_authenticated:
        return request.user, True

    # 비회원일 경우 UUID 기반의 더미 사용자 생성
    temp_email = f"guest_{uuid.uuid4().hex[:10]}@example.com"
    
    # 비회원용 User 객체 생성 (저장)
    user = User.objects.create(email=temp_email, password="guest_password")
    
    return user, False

def info_submit(request):
    if request.method == "POST":

        # 회원일 경우 이메일 반환, 비회원일 경우 생성해서 반환
        user, check = get_or_create_user(request)

        # ✅ 섹션 건너뛰기 여부
        marital_skipped = bool(request.POST.get("marriage_skip_btn"))
        children_skipped = bool(request.POST.get("children_skip_btn"))
        other_skipped = bool(request.POST.get("other_skip_btn"))
        detail_skipped = bool(request.POST.get("detail_skip_btn"))

        # ✅ 혼인 관련
        marital_status = None
        marriage_duration = None
        divorce_status = None

        if not marital_skipped:
            marital_status = request.POST.get("marriage_status")
            duration_raw = request.POST.get("marriage_duration")
            marriage_duration = request.POST.get("marriage_duration")
            divorce_status = request.POST.get("divorce_status")

        # ✅ 자녀 관련
        has_children = None
        children_ages = None

        if not children_skipped:
            has_children = request.POST.get("child_status") == "yes"
            children_ages = request.POST.get("child_age")

        # ✅ 기타 정보
        property_range = None
        experience = None

        if not other_skipped:
            property_range = request.POST.get("property_scope")
            experience = request.POST.get("experience")

        # ✅ 고민 정보
        detail_info = None

        if not detail_skipped:
            detail_info = request.POST.get("detail_info")

        # ✅ DB 저장
        UserInfo.objects.create(
            user=user,
            marital_skipped=marital_skipped,
            marital_status=marital_status,
            marriage_duration=marriage_duration,
            divorce_status=divorce_status,

            children_skipped=children_skipped,
            has_children=has_children,
            children_ages=children_ages,

            other_skipped=other_skipped,
            property_range=property_range,
            experience=experience,

            detail_skipped=detail_skipped,
            detail_info=detail_info
        )

        return redirect("user:home")  # or "chat" 페이지로 변경 예정
    return redirect("user:info")