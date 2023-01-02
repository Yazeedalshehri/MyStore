from django.shortcuts import render ,redirect , get_object_or_404
from django.http import request
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import login , authenticate
from django.core.paginator import Paginator
from .models import Admins , product


def HomePage(request):
    context = {'Admins' : Admins}
    return render(request,"HomePage.html",context)


def Register(request ):
    if request.method == 'POST' :
       username = request.POST['username'] 
       email = request.POST['email'] 
       password = request.POST['password'] 
       phonenumber = request.POST['phonenumber'] 
       new_admin = Admins(username=username, email=email, password=password,phonenumber=phonenumber)
       new_admin.save()
        
       return redirect (AdminPage , slug = username)

    return render(request,"Register.html")


def Login(request):
    return render(request,"login.html")

def AdminPage(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    context = {'admin': AdminPage}
    return render(request,"AdminPage.html", context)

def Analytics(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    context = {'admin': AdminPage}
    return render(request,"Analytics.html",context)

def Customers(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    context = {'admin': AdminPage}
    return render(request,"Customers.html",context)


def Orders(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    context = {'admin': AdminPage}
    return render(request,"Orders.html",context)


def Products(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    pro=product.objects.all()
    context = {'admin': AdminPage , 'prod': pro}
    if request.method == 'POST' :
        Name = request.POST['Name'] 
        Number = request.POST['Number'] 
        Quantity = request.POST['Quantity'] 
        Price = request.POST['Price']   
        Description = request.POST['Description']  
        img = request.POST['img']   
        new_products= product(Admins=AdminPage ,PRDname=Name,PRDnumber=Number,quantity=Quantity,price=Price,desc=Description,PRDimage=img)
        new_products.save()
    return render(request,"Products.html",context)


def Settings(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    context = {'admin': AdminPage}
    return render(request,"Settings.html",context)
