from django.shortcuts import render
from django.http import request


def HomePage(request):
    return render(request,"HomePage.html")


def Register(request):
    return render(request,"Register.html")
# Create your views here.

def Login(request):
    return render(request,"login.html")

def AdminPage(request):
    return render(request,"AdminPage.html")

def Analytics(request):
    return render(request,"Analytics.html")

def Customers(request):
    return render(request,"Customers.html")


def Orders(request):
    return render(request,"Orders.html")


def Products(request):
    return render(request,"Products.html")


def Settings(request):
    return render(request,"Settings.html")
