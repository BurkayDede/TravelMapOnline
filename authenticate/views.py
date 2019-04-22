from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def home(request):
    return render(request, 'authenticate/home.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login_user')
    else:
        return render(request, 'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    return redirect('home')