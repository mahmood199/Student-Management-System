
from django.shortcuts import render, redirect
from django.template import context
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def HOME(request):
    return render(request, 'hod/home.html')