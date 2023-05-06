
from django.shortcuts import render, redirect
from django.template import context


def HOME(request):
    return render(request, 'hod/home.html', context)