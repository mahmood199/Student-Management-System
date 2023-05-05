from django.shortcuts import render, redirect
from django.template import Template

def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')