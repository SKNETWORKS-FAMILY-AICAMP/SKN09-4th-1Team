from django.shortcuts import render, redirect
from user.views import get_or_create_user
from django.utils import timezone
from .models import Chat, Message
from user.models import User  
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# from user.models import User  # 또는 get_or_create_user로 대체 가능
from django.contrib.auth import login
from user.services.auth_service import authenticate_user
from django.views.decorators.http import require_POST
from django.http import JsonResponse


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate_user(email, password)
        if user:
            # login(request, user)
            request.session['user_id'] = str(user.id)
            request.session['user_email'] = user.email
            next_url = request.GET.get('next') or 'chat:member_start'
            return redirect(next_url)

# 유진 시작
def get_or_create_guest_user(request):
    # 이미 세션에 있으면 해당 사용자 반환
    user_id = request.session.get("guest_user_id")
    if user_id:
        try:
            return User.objects.get(id=user_id), False
        except User.DoesNotExist:
            pass  # 만료 등 예외 처리

    # 없으면 새 Guest 생성
    guest_email = f"guest_{uuid.uuid4().hex[:10]}@example.com"
    user = User.objects.create(email=guest_email, password="guest_password")
    request.session["guest_user_id"] = str(user.id)  # 세션에 저장
    request.session["user_email"] = guest_email  # (선택) 상단 표시용
    return user, True

def chat_guest_start(request):
    
    user, created = get_or_create_guest_user(request)

    return render(request, 'chat/chat_guest_00.html')

def chat_guest_save(request):
    if request.method == "POST":
        # 1. 세션에서 비회원 ID 가져오기
        user_id = request.session.get("guest_user_id")
        if not user_id:
            return redirect("chat:chat_guest_start")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return redirect("chat:chat_guest_start")

        # 2. 사용자 입력값
        user_input = request.POST.get("user_input")
        if not user_input:
            return redirect("chat:chat_guest_start")

        # 3. Chat 생성
        chat = Chat.objects.create(
            user=user,
            chat_title=user_input,  # 질문을 채팅 제목으로, 히스토리에서 잘라서 보여줄 것
            created_at=timezone.now()
        )

        # 4. Message 생성
        Message.objects.create(
            chat=chat,
            sender='user',
            message=user_input,
            created_at=timezone.now()
        )

        # 4-2. Bot 응답 메시지도 저장
        Message.objects.create(
            chat=chat,
            sender='bot',
            message="준비된 답변입니다.",
            created_at=timezone.now()
        )

        # 5. 채팅 상세 화면으로 이동
        return redirect('chat:guest_chat_with_id', chat_id=chat.id)

    # POST가 아니면 다시 시작 화면으로
    return redirect("chat:chat_guest_start")

@csrf_exempt
def chat_guest(request, chat_id):
    chat = Chat.objects.get(id=chat_id)

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        if user_input:
            Message.objects.create(
                chat=chat,
                sender="user",
                message=user_input,
                created_at=timezone.now()
            )
            # 여기선 봇 응답도 더미로 저장할 수 있음
            Message.objects.create(
                chat=chat,
                sender="bot",
                message="준비된 답변입니다.",
                created_at=timezone.now()
            )
            return redirect('chat:guest_chat_with_id', chat_id=chat.id)

    messages = Message.objects.filter(chat=chat).order_by('created_at')
    return render(request, 'chat/chat_guest_01.html', {
        'chat': chat,
        'messages': messages,
    })
# 유진 끝 

# 멤버 채팅 시작 화면면
# @login_required(login_url='/')
def chat_member_start(request):
    # # ⚠️ 개발용 사용자 강제 설정 (실제로는 삭제해야 함!)
    # if not request.user.is_authenticated:
    #     request.user = User.objects.get(email='test@example.com')  # 존재하는 회원이어야 함
    
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/')  # 로그인 페이지로

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('/')
    
    return render(request, 'chat/chat_member_00.html')

def chat_member_save(request):
    if request.method == "POST":
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("/")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return redirect("/")

        user_input = request.POST.get("user_input")
        if not user_input:
            return redirect("chat:member_start")

        chat = Chat.objects.create(
            user=user,
            chat_title=user_input,
            created_at=timezone.now()
        )

        Message.objects.create(chat=chat, sender='user', message=user_input, created_at=timezone.now())
        Message.objects.create(chat=chat, sender='bot', message="준비된 답변입니다.", created_at=timezone.now())

        return redirect('chat:member_chat_with_id', chat_id=chat.id)

    return redirect("chat:member_start")

def chat_member(request, chat_id):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("/")

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect("/")

    chat = Chat.objects.get(id=chat_id)
    if chat.user != user:
        return redirect("chat:member_start")

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        if user_input:
            Message.objects.create(chat=chat, sender="user", message=user_input, created_at=timezone.now())
            Message.objects.create(chat=chat, sender="bot", message="준비된 답변입니다.", created_at=timezone.now())
            return redirect('chat:member_chat_with_id', chat_id=chat.id)

    messages = Message.objects.filter(chat=chat).order_by('created_at')
    chat_list = Chat.objects.filter(user=user).order_by('-created_at')
    
    return render(request, 'chat/chat_member_01.html', {
        'chat': chat,
        'messages': messages,
        'chat_list':chat_list,
    })

@require_POST
def chat_member_delete(request, chat_id):
    chat = Chat.objects.get(id=chat_id, user=request.user)
    chat.delete()
    return JsonResponse({'status': 'ok'})


def chat_entry(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return redirect('/')
        latest_chat = Chat.objects.filter(user=user).order_by('-created_at').first()
        if latest_chat:
            return redirect('chat:member_chat_with_id', chat_id=latest_chat.id)
        else:
            return redirect('chat:member_start')
    else:
        return redirect('chat:chat_guest_start')
