from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),

    ### 로그아웃 기능 확인용임 삭제해야함 #### ####### #######
    path('logout/', views.logout_view, name='logout'),
    ####### ####### ####### ####### ####### ####### #######

    path('password/', views.find_password, name='find_password'),
    path('password/complete/', views.find_password_complete, name='find_password_complete'),
    path('info/', views.info, name='info'),
    path('info/submit', views.info_submit, name='info_submit'), 
    path('info/cancel', views.info_cancel, name='info_cancel'), 

    path('join/', views.join_user_form, name='join_01'),
    path('join/popup_service', views.join_terms_service, name='join_terms_service'),
    path('join/popup_privacy', views.join_terms_privacy, name='join_terms_privacy'),
    path('join/email', views.join_user_email_form, name='join_02'),
    path('join/email/certification', views.join_user_email_certification, name='join_03'),
    path('join/complete/', views.join_user_complete, name='join_04'), 

]