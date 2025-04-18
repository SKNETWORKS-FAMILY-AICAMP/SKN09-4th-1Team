from django.shortcuts import render, redirect
from user.views import get_or_create_user
from django.utils import timezone
from .models import Chat, Message
from user.models import User  
import uuid
from django.views.decorators.csrf import csrf_exempt
# from user.models import User  # 또는 get_or_create_user로 대체 가능


def home(request):
    return render(request, 'user/home_01.html')

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

# 멤버 채팅 시작 화면
def chat_member_start(request):
    return render(request, 'chat/chat_member_00.html')

# 게스트 채팅 화면
def chat_guest(request, chat_id=None):
    chat = None
    messages = []

    if chat_id:
        chat = Chat.objects.get(id=chat_id)
        messages = Message.objects.filter(chat=chat).order_by('created_at')

    context = {
        'chat': chat,
        'messages': messages,
    }

    return render(request, 'chat/chat_guest_01.html', context)

# 멤버 채팅 화면
def chat_member(request):
    # chat_id에 따른 채팅 화면을 보여줌
    return render(request, f'chat/chat_member_01.html')



def chat_entry(request):
    user, is_registered = get_or_create_user(request)

    if is_registered:
        return redirect('chat:member_chat')  # 회원용 채팅 화면
    else:
        return redirect('chat:guest_chat')   # 비회원용 채팅 화면
    