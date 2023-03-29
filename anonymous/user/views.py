from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from user.models import User

def signin(request) :
    if request.method == 'GET' :
        return render(request, 'page/signin.html')
    if request.method =='POST' :
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)
        if user :
            login(request, user)
            return redirect('board')
        else :
            messages.error(request, '입력값을 확인해 주세요.')
            return redirect('signin')
        
def signup(request) :
    if request.method == 'GET' :
        
        return render(request, 'page/signup.html')

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        nickname = request.POST['nickname']
        
        user = User.objects.filter(username=username)
        if user.exists() : 
            messages.error(request, '이미 존재하는 아이디입니다.')
            return redirect('signup')

        else :
            new_user = User(
                            username = username,
                            password=make_password(password),
                            nickname=nickname
                            )
            new_user.save()
            login(request, new_user)
            return redirect('board')
            
def signout(request) :
    if request.method == 'GET' :
        logout(request)
        return redirect('board')
        