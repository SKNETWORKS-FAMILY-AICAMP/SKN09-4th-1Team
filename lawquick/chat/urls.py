from django.urls import path
from . import views

app_name = 'chat'  # 네임스페이스 설정

urlpatterns = [
    path('', views.chat_entry, name='chat_entry'),  # ✅ 자동 분기 포인트

    # 게스트 채팅 플로우
    path('guest/00/', views.chat_guest_start, name='chat_guest_start'),
    path('chat/guest/01/', views.chat_guest_save, name='chat_guest_save'),
    path('guest/chat/<int:chat_id>/', views.chat_guest, name='guest_chat_with_id'),

    # 멤버 채팅
    path('member/00/', views.chat_member_start, name='member_start'),
    path('chat/member/01/', views.chat_member_save, name='chat_member_save'),
    path('member/chat/<int:chat_id>/', views.chat_member, name='member_chat_with_id'),

    # ✅ 사이드바에서 사용하는 삭제 + 수정
    path('member/delete/<int:chat_id>/', views.chat_member_delete, name='member_chat_delete'),
    path('member/update-title/<int:chat_id>/', views.chat_member_update_title, name='member_chat_update_title'),  # ← 추가!
]
