from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from user.models import User
from .models import Chat, Message
import uuid
import datetime

# 공통 진입점 (회원/비회원 분기)
def chat_entry(request):
    if request.session.get('guest'):
        return redirect('chat:main')
    elif request.session.get('user_id'):
        return redirect('chat:main')
    else:
        return redirect('user:home')

# 메인 채팅 페이지
def chat_main(request):
    is_guest = request.session.get("guest", False)
    user_id = request.session.get("user_id")
    guest_user_id = request.session.get("guest_user_id")
    chat_list, current_chat, messages = [], None, []
    user_email = request.session.get("user_email")

    if user_id and not is_guest:
        try:
            user = User.objects.get(id=user_id)
            chat_list = Chat.objects.filter(user=user).order_by('-created_at')
            current_chat = chat_list.first()
        except User.DoesNotExist:
            return redirect('user:home')

    elif is_guest and guest_user_id:
        try:
            user = User.objects.get(id=guest_user_id)
            chat_list = Chat.objects.filter(user=user).order_by('-created_at')
            current_chat = chat_list.first()
        except User.DoesNotExist:
            return redirect('chat:chat_guest_view')

    else:
        return redirect('user:home')

    if current_chat:
        messages = Message.objects.filter(chat=current_chat).order_by('created_at')

    return render(request, 'chat/chat.html', {
        'chat_list': chat_list,
        'current_chat': current_chat,
        'chat_messages': messages,
        'is_guest': is_guest,
        'user_email': user_email,
    })

# 채팅 제목 클릭 시 해당 채팅으로 이동
@require_POST
def chat_member_start(request, chat_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user:home')

    try:
        user = User.objects.get(id=user_id)
        chat = Chat.objects.get(id=chat_id, user=user)
    except (User.DoesNotExist, Chat.DoesNotExist):
        return redirect('chat:main')

    chat_list = Chat.objects.filter(user=user).order_by('-created_at')
    messages = Message.objects.filter(chat=chat).order_by('created_at')
    user_email = request.session.get('user_email')

    return render(request, 'chat/chat.html', {
        'chat_list': chat_list,
        'current_chat': chat,
        'chat_messages': messages,
        'user_email': user_email,
        'is_guest': False,
    })

# 채팅 메시지 전송
@require_POST
@csrf_exempt
def chat_send(request):
    if request.method == "POST":
        is_guest = request.session.get('guest', False)
        user_id = request.session.get("guest_user_id") if is_guest else request.session.get("user_id")

        if not user_id:
            return redirect('user:home')

        message = request.POST.get("message", "").strip()
        if not message:
            return redirect("chat:main")

        user = User.objects.get(id=user_id)
        chat = Chat.objects.filter(user=user).order_by('-created_at').first()
        if not chat:
            chat = Chat.objects.create(user=user, chat_title=message[:10])

        # 사용자 메시지 저장
        Message.objects.create(chat=chat, sender="user", message=message)

        # 가상 AI 응답
        dummy_answer = "이혼 및 양육권 관련 법률 정보와 절차는 다음과 같습니다..."
        Message.objects.create(chat=chat, sender="bot", message=dummy_answer)

        # 현재 시각 및 출력 소요 시간
        now = timezone.localtime()
        now_time = now.strftime("%I:%M %p").lower()
        output_duration = "출력 소요 시간: 75s"

        return render(request, "chat/chat_talk.html", {
            "user_message": message,
            "bot_answer": dummy_answer,
            "now_time": now_time,
            "output_duration": output_duration,
            "is_guest": is_guest,
        })

    return redirect('chat:main')


# 채팅 삭제
@require_POST
@csrf_exempt
def chat_member_delete(request, chat_id):
    try:
        chat = Chat.objects.get(id=chat_id)
        user_id = request.session.get('user_id')

        if not user_id or str(chat.user.id) != str(user_id):
            return JsonResponse({'status': 'unauthorized'}, status=403)

        chat.delete()
        return JsonResponse({'status': 'ok'})
    except Chat.DoesNotExist:
        return JsonResponse({'status': 'not_found'}, status=404)

# 채팅 제목 수정
@require_POST
@csrf_exempt
def chat_member_update_title(request, chat_id):
    import json
    try:
        chat = Chat.objects.get(id=chat_id)
        user_id = request.session.get('user_id')

        if not user_id or str(chat.user.id) != str(user_id):
            return JsonResponse({'status': 'unauthorized'}, status=403)

        data = json.loads(request.body)
        new_title = data.get('title', '').strip()
        if new_title:
            chat.chat_title = new_title
            chat.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'empty_title'}, status=400)
    except Chat.DoesNotExist:
        return JsonResponse({'status': 'not_found'}, status=404)

# 비회원 시작용 guest 세션 생성
def chat_guest_view(request):
    request.session.flush()
    request.session['guest'] = True

    guest_email = f"guest_{uuid.uuid4().hex[:10]}@example.com"
    guest_user = User.objects.create(email=guest_email, password='guest_pw')
    request.session['guest_user_id'] = str(guest_user.id)
    request.session['user_email'] = guest_email

    return redirect('chat:main')

# 가상 답변 테스트용 뷰
def chat_talk_view(request):
    if request.method == "POST":
        message = request.POST.get("message", "").strip()
        if not message:
            return redirect('chat:chat_talk')

        is_guest = request.session.get('guest', False)
        now = timezone.localtime()
        now_time = now.strftime("%I:%M %p").lower()

        dummy_answer = (
            "1. 관련 법률 조항\n"
            "민법 제909조 제2항은 부모가 자녀의 양육에 관한 권리와 의무를 가진다고 규정하고 있으며...\n\n"
            "2. 주요 판례 요약\n"
            "대법원 2001다20243 판결에서는 양육권을 결정할 때 자녀의 나이, 양육 환경, 경제력, 자녀의 의사 등을 종합적으로 고려해야 한다고 보았습니다.\n\n"
            "3. 일반적인 법적 해석\n"
            "법원은 자녀의 복리를 최우선으로 고려합니다. 자세한 내용은 전문가 상담을 권장드립니다."
        )
        output_duration = "출력 소요 시간: 75s"

        if is_guest:
            session_chat = request.session.get('guest_chat', [])
            session_chat.append({
                'question': message,
                'answer': dummy_answer,
                'time': now_time,
                'duration': output_duration
            })
            request.session['guest_chat'] = session_chat

        else:
            user_id = request.session.get('user_id')
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return redirect('user:home')

            chat = Chat.objects.create(
                user=user,
                chat_title=message[:20],
            )

            Message.objects.create(
                chat=chat,
                role='user',
                message=message,
            )

            Message.objects.create(
                chat=chat,
                role='bot',
                message=dummy_answer,
            )

        return render(request, 'chat/chat_talk.html', {
            'user_message': message,
            'bot_answer': dummy_answer,
            'now_time': now_time,
            'output_duration': output_duration,
            'is_guest': is_guest,
        })

    return render(request, 'chat/chat_talk.html')
