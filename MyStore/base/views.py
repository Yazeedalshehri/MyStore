from django.shortcuts import render ,redirect , get_object_or_404
from django.http import request
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import login , authenticate
from django.core.paginator import Paginator
from .models import Admins , product
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import AdminsForm
from django.views.generic import CreateView 


def HomePage(request):
    context = {'Admins' : Admins}
    return render(request,"HomePage.html",context)

def UserLogin(request):
     return render(request,"UserLogin.html")

def Cart(request):
     return render(request,"CartPage.html")     


def Login(request):
    if request.method == 'POST' :
        username = request.POST['username'] 
        password = request.POST['password']
        mydata= Admins.objects.get(slug = username , password = password) 
        return redirect (AdminPage , slug = mydata.slug )
        
    return render(request,"Login.html")

def signup (request):
    if request.method == 'POST':
        form = AdminsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(AdminPage , slug = form.username)
    else:
        form = AdminsForm()
    return render(request,
                  'Register.html',
                  {'form': form}

                  )


def Register(request ):
    if request.method == 'POST' :
       username = request.POST['username'] 
       email = request.POST['email'] 
       password = request.POST['password'] 
       phonenumber = request.POST['phonenumber'] 
       storename = request.POST['storename'] 
       new_admin = Admins(username=username, email=email, password=password,phonenumber=phonenumber,storename=storename )
       new_admin.save()
       if request.POST.get('category'):
            new_admin.category=request.POST.get('category')
            new_admin.save()
       return redirect (AdminPage , slug = username)
    return render(request,"Register.html")



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
    if request.POST.get('StoreColor'):
        AdminPage.storecolor=request.POST.get('StoreColor')
        AdminPage.save()
    if request.POST.get('StoreName'):
        AdminPage.storename=request.POST.get('StoreName')
        AdminPage.save()
        
    return render(request,"Settings.html",context)

def Store(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    pro=product.objects.all()
    context = {'admin': AdminPage , 'prod': pro}
    return render(request,"carstore.html",context)

def Cart(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    context = {'admin': AdminPage}
    return render(request,"CartPage.html",context)

def userlogin(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    context = {'admin': AdminPage}
    return render(request,"UserLogin.html",context)
    