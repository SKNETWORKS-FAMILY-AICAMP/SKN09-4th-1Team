from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.join_01, name='join_01'),
]
