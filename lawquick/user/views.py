from django.shortcuts import render

def home(request):
    return render(request, 'user/home_01.html')