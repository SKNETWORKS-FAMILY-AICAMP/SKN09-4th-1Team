from django.urls import path
from . import views

app_name = 'chat'  # 네임스페이스 설정

urlpatterns = [
    path('', views.chat_entry, name='chat_entry'),  # ✅ 자동 분기 포인트
    
    # path('guest/chat/', views.chat_guest_empty, name='guest_chat'),  # <- chat_id 없이 진입

    # 시작 화면
    path('guest/00/', views.chat_guest_start, name='chat_guest_start'),
    path('member/00/', views.chat_member_start, name='member_start'),  # ✅ 여기 name='member_start'

    path('chat/member/00/', views.chat_member_start, name='chat_member_start'),

    path('guest/chat/<int:chat_id>/', views.chat_guest, name='guest_chat_with_id'),
    
    # 실제 채팅 화면
    path('chat/guest/01/', views.chat_guest, name='chat_guest'),
    path('chat/member/01/', views.chat_member, name='chat_member'),
]
