from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from user.models import User
from .models import Chat, Message
import uuid
import datetime
from user.models import UserInfo
import requests

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
    user_email = request.session.get("user_email")

    chat_list, current_chat, messages = [], None, []

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
    is_guest = request.session.get('guest', False)
    user_id = request.session.get("guest_user_id") if is_guest else request.session.get("user_id")

    if not user_id:
        return redirect('user:home')

    message = request.POST.get("message", "").strip()
    if not message:
        return redirect("chat:main")

    user = User.objects.get(id=user_id)

    # 새 채팅 생성
    chat = Chat.objects.create(user=user, chat_title=message[:20])

    # 메시지 저장
    Message.objects.create(chat=chat, sender="user", message=message)
    dummy_answer = "이혼 및 양육권 관련 법률 정보와 절차는 다음과 같습니다..."
    Message.objects.create(chat=chat, sender="bot", message=dummy_answer)

    # chat_id로 redirect
    return redirect('chat:chat_talk_detail', chat_id=chat.id)


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

def chat_talk_view(request, chat_id):
    is_guest = request.session.get('guest', False)
    user_email = request.session.get("user_email")

    try:
        chat = Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return redirect('chat:main')

    # 🔐 사용자 검증
    user_id = request.session.get("guest_user_id") if is_guest else request.session.get("user_id")
    if not user_id or str(chat.user.id) != str(user_id):
        return redirect('chat:main')


    # ✅ POST 요청: 질문 저장 + RunPod 모델 호출
    if request.method == "POST":
        message = request.POST.get("message", "").strip()
        if message:
            # 1. 질문 저장
            Message.objects.create(chat=chat, sender='user', message=message)

            # 2. 유저 정보 불러오기
            try:
                info = UserInfo.objects.get(user=chat.user)
                user_info = {
                    "marital_status": info.marital_status,
                    "marriage_duration": info.marriage_duration,
                    "divorce_status": info.divorce_status,
                    "has_children": info.has_children,
                    "children_ages": info.children_ages,
                    "experience": info.experience,
                    "property_range": info.property_range,
                    "detail_info": info.detail_info,
                }
            except UserInfo.DoesNotExist:
                user_info = {}

            # 3. RunPod API 호출
            try:
                api_url = "http://x76r8kryd0u399-7004.proxy.runpod.net/chat"
                payload = {
                    "message": message,
                    "user_info": user_info
                }
                res = requests.post(api_url, json=payload, timeout=60)
                res.raise_for_status()
                data = res.json()
                answer = data.get("response", "⚠️ 응답이 없습니다.")
            except Exception as e:
                answer = f"❗ 오류 발생: {str(e)}"

            # 4. 응답 저장
            Message.objects.create(chat=chat, sender='bot', message=answer)

        return redirect('chat:chat_talk_detail', chat_id=chat.id)

    # ✅ GET 요청: 채팅 화면 렌더링
    messages = Message.objects.filter(chat=chat).order_by('created_at')
    chat_list = Chat.objects.filter(user=chat.user).order_by('-created_at')
    now = timezone.localtime()
    now_time = now.strftime("%I:%M %p").lower()

    return render(request, "chat/chat_talk.html", {
        "messages": messages,
        "current_chat": chat,
        "chat_list": chat_list,
        "user_email": user_email,
        "is_guest": is_guest,
        "now_time": now_time,
    })