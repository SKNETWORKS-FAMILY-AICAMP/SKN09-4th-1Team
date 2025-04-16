from django.shortcuts import render, redirect
from django.contrib import messages
from .services.auth_service import authenticate_user
from .repositories.user_repository import user_exists_by_email, get_user_by_email

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

            # ✅ [임시 코드] 세션 기반 로그인 확인 메시지 (향후 삭제 예정)
            ######## ###### ###### ###### ###### ###### ###### ###### 
            request.session['user_email'] = user.email
            ####### ####### ###### ###### ###### ###### ###### ######

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
