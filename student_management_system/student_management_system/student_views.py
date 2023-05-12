
from django.shortcuts import render, redirect


@login_required(login_url='/')
def Home(request):
    return render(request,'Student/home.html')