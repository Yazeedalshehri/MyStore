from django.shortcuts import render
from django.http import request
from .models import Admins


def HomePage(request):
    return render(request,"HomePage.html")


def Register(request):
    if request.method == 'POST' :
       username = request.POST['username'] 
       email = request.POST['email'] 
       password = request.POST['password'] 
       phonenumber = request.POST['phonenumber'] 
       new_admin = Admins(username=username, email=email, password=password,phonenumber=phonenumber)
       new_admin.save()
    return render(request,"Register.html")


def Login(request):
    return render(request,"login.html")