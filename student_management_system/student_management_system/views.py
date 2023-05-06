from django.shortcuts import render, redirect, HttpResponse
from django.template import Template
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, logout, login


def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackend.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'), )
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return HttpResponse('This is Hod Panel')
            elif user_type == '2':
                return HttpResponse('This is Staff Panel')
            elif user_type == '3':
                return HttpResponse('This is Student Panel')
            else:
                messages.error(request, 'Email and Password Are Invalid !')
                return redirect('login')
        else:
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')
