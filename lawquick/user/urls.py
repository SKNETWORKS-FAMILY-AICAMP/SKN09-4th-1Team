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
]