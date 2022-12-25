from django.shortcuts import render
from django.http import request


def HomePage(request):
    return render(request,"HomePage.html")
# Create your views here.
