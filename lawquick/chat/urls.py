from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # 채팅 시작 화면 (게스트, 멤버 선택)
    path('chat/guest/00/', views.chat_guest_start, name='chat_guest_start'),
    path('chat/member/00/', views.chat_member_start, name='chat_member_start'),
    
    # 게스트/멤버 채팅 화면 (각각의 채팅 화면)
    path('chat/guest/01/', views.chat_guest, name='chat_guest'),
    path('chat/member/01/', views.chat_member, name='chat_member'),
]
