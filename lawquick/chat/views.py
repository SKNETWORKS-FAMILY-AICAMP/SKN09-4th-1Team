from django.shortcuts import render, redirect
from user.views import get_or_create_user
from django.utils import timezone
from .models import Chat, Message
# from user.models import User  # 또는 get_or_create_user로 대체 가능


def home(request):
    return render(request, 'user/home_01.html')

def chat_guest_start(request):
    if request.method == 'POST':
        question = request.POST.get('user_input')
        
        # 유저 가져오기 또는 생성
        guest_user, _ = get_or_create_user(email="guest@example.com")

        # Chat 생성
        chat = Chat.objects.create(user=guest_user, chat_title=question)

        # 사용자 메시지 저장
        Message.objects.create(
            chat=chat,
            sender='user',
            message=question,
            created_at=timezone.now()
        )

        # chat_guest 뷰로 이동 (chat_id를 URL에 전달)
        return redirect('chat:guest_chat_with_id', chat_id=chat.id)  

    return render(request, 'chat/chat_guest_00.html')

# 멤버 채팅 시작 화면
def chat_member_start(request):
    return render(request, 'chat/chat_member_00.html')

# 게스트 채팅 화면
def chat_guest(request, chat_id):
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