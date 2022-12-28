from django.shortcuts import render
from django.http import request


def HomePage(request):
    return render(request,"HomePage.html")


def Register(request):
    return render(request,"Register.html")
# Create your views here.

def Login(request):
    return render(request,"login.html")