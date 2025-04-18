from django.shortcuts import render, redirect

def home(request):
    return render(request, 'user/home_01.html')

def find_password(request):
    if request.method == 'POST':
        return redirect('user:find_password_email_confirm')
    return render(request, 'user/search_01.html')


def find_password_email_confirm(request):
    if request.method == 'POST':
        return redirect('user:find_password_complete')
    return render(request, 'user/search_02.html')

def find_password_complete(request):
    return render(request, 'user/search_03.html')

def info(request):
    if request.method == 'POST':
        return redirect('user:info')
    return render(request, 'user/info.html')