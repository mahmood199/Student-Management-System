from django.shortcuts import render, redirect, HttpResponse
from django.template import Template
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser


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
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, 'Email and Password Are Invalid !')
                return redirect('login')
        else:
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.FILES.get('first_name')
        last_name = request.FILES.get('last_name')
        email = request.FILES.get('email')
        username = request.FILES.get('username')
        password = request.FILES.get('password')

        try:
            customUser = CustomUser.object.get(id=request.user.id)

            customUser.first_name = first_name
            customUser.last_name = last_name

            if password is not None and password != "":
                customUser.set_password(password)
            if profile_pic is not None and profile_pic != "":
                customUser.profile_pic = profile_pic
            customUser.save()
            messages.success(request, 'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request, 'Failed To Update Your Profile')
    return render(request, 'profile.html')
