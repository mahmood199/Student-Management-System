from app.models import Course, Session_Year, CustomUser, Student, Staff, Subject
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(login_url='/')
def HOME(request):
    return render(request, 'staff/home.html')