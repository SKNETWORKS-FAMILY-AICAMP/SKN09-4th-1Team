from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.find_password, name='find_password'),
    path('password/confirm/', views.find_password_email_confirm, name='find_password_email_confirm'),
    path('password/complete/', views.find_password_complete, name='find_password_complete'),
    path('info/', views.info, name='info'),
    path('info/submit', views.info_submit, name='info_submit'), 

]