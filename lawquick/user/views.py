from django.shortcuts import render

def home(request):
    return render(request, 'user/home_01.html')

def find_password(request):
    return render(request, 'user/search_01.html')