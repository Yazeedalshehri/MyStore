from django.shortcuts import render ,redirect , get_object_or_404
from django.http import request
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import login , authenticate
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import AdminsForm
from django.views.generic import CreateView 
from django.http import JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt
from .utils import cartData 
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect




def HomePage(request):
    context = {'Admins' : Admins}
    return render(request,"HomePage.html",context)

def UserLogin(request):
     return render(request,"UserLogin.html")

def Cart(request):
     return render(request,"CartPage.html")     


def Login(request):
    admins = Admins.objects.all()
    if request.method == 'POST' :
        username = request.POST['username'] 
        password = request.POST['password']
        for i in admins:
            if i.username == username and i.password==password :
                mydata= Admins.objects.get(slug = username , password = password) 
                return redirect (AdminPage , slug = mydata.slug )
       
    return render(request,"Login.html")


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
    Orders = CompletedOrder.objects.all()
    
    totalSales = 0
    NumberOfOrders = 0
    AvargeSales = 0
    for i in Orders :
        if i.Admins.slug == AdminPage.slug: 
            totalSales += i.total
            NumberOfOrders += 1

    if NumberOfOrders != 0 :   
        AvargeSales = totalSales/NumberOfOrders
    context = {'admin': AdminPage , 'totalSales': totalSales, 'NumberOfOrders': NumberOfOrders , 'AvargeSales' : AvargeSales , 'Orders':Orders}
    return render(request,"AdminPage.html", context)

def Analytics(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    Orders = CompletedOrder.objects.all()
    totalSales = 0
    NumberOfOrders = 0
    AvargeSales = 0
    for i in Orders :
        if i.Admins.slug == AdminPage.slug: 
            totalSales += i.total
            NumberOfOrders += 1

    if NumberOfOrders != 0 :   
        AvargeSales = int(totalSales/NumberOfOrders)
    context = {'admin': AdminPage , 'totalSales': totalSales, 'NumberOfOrders': NumberOfOrders , 'AvargeSales' : AvargeSales}
    
    return render(request,"Analytics.html",context)

def Customers(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    CustomerInfo = CompletedOrder.objects.all()
    

    context = {'admin': AdminPage , 'CustomerInfo': CustomerInfo}
    return render(request,"Customers.html",context)


def Orders(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    orders = CompletedOrder.objects.all()
       
    context = {'admin': AdminPage , 'Orders': orders}
    return render(request, 'Orders.html',context)        

def Products(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    pro=product.objects.all()
    context = {'admin': AdminPage , 'prod': pro}
    if request.method == 'POST':
        Name = request.POST['Name'] 
        Number = request.POST['Number'] 
        Quantity = request.POST['Quantity'] 
        Price = request.POST['Price']   
        Description = request.POST['Description']  
        img = request.FILES['img']   
        new_products= product(Admins=AdminPage ,PRDname=Name,PRDnumber=Number,quantity=Quantity,price=Price,desc=Description,PRDimage=img)
        new_products.save() 
     
    return render(request,"Products.html",context)

def DeleteProduct(request,PRDNumber,slug):
        DeleteQuery = product.objects.get(PRDnumber = PRDNumber)
        DeleteQuery.delete()  
        AdminPage= get_object_or_404(Admins , slug=slug)
        pro=product.objects.all()
        context = {'admin': AdminPage , 'prod': pro}
        return render(request,"Products.html",context)
       # return HttpResponseRedirect(reverse(render(request,"Products.html",context)))
        

def Settings(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    context = {'admin': AdminPage}
    if request.POST.get('StoreColor'):
        AdminPage.storecolor=request.POST.get('StoreColor')
        AdminPage.save()
    if request.POST.get('StoreTextColor'):
        AdminPage.StoreTextColor=request.POST.get('StoreTextColor')
        AdminPage.save()    
    if request.POST.get('StoreName'):
        AdminPage.storename=request.POST.get('StoreName')
        AdminPage.save()
    if request.POST.get('email'):
        AdminPage.storeEmail=request.POST.get('email')
        AdminPage.save()
    if request.POST.get('Phone'):
        AdminPage.StorePhone=request.POST.get('Phone')
        AdminPage.save()
    if request.POST.get('StoreBackgroundColor'):
        AdminPage.StoreBackgroundColor=request.POST.get('StoreBackgroundColor')
        AdminPage.save()    
        
    return render(request,"Settings.html",context)

def Store(request , slug ):
    AdminPage= get_object_or_404(Admins , slug=slug)
    AdminName = Admins.objects.all()
    pro=product.objects.all()
    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = product.objects.all()
    context = {'admin': AdminPage , 'prod': pro ,'products':products, 'cartItems':cartItems}
       
    return render(request,"carstore.html",context)

def Cart(request , slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    
    context = {'admin': AdminPage ,'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,"CartPage.html",context )

def userlogin(request , slug):
   AdminPage= get_object_or_404(Admins , slug=slug)
   context = {'admin': AdminPage}
   return render(request,"UserLogin.html",context)

def UserLoginView(request ,slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    if request.method == 'POST':
        Name = request.POST['name'] 
        Email = request.POST['email'] 
        password = request.POST['password'] 
        Phonenumber = request.POST['phonenumber']   
        new_User = User(Name= Name, Email= Email, password = password, Phonenumber= Phonenumber)
        new_User.save()  
        
   

        
    return render(request,"UserLogin.html")


@csrf_exempt
def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(action)
    print(productId)
    customer = request.user.customer
    ProductObject = product.objects.get(PRDnumber=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, Product=ProductObject)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()



     
     
    return JsonResponse('Item was added', safe=False)
   

def Checkout(request ,slug):
    AdminPage= get_object_or_404(Admins , slug=slug)
    data = cartData(request)
	
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    price = data['price']
    if request.method == 'POST':
        Name = request.POST['name'] 
        Email = request.POST['email'] 
        Phonenumber = request.POST['phonenumber']   
        Address = request.POST['address']
        City = request.POST['city']
        State = request.POST['state']
        Zipcode = request.POST['zipcode']
        new_ShippingAdress = ShippingAddress(name=Name,Phone=Phonenumber,email=Email,address=Address,city=City,state=State,zipcode=Zipcode)
        new_ShippingAdress.save()
        Complete_order = CompletedOrder(Admins = AdminPage, Customer=new_ShippingAdress,Order=order)
        Complete_order.total=price
        Complete_order.save()
        OrderItem.objects.all().delete()

    context = {'admin': AdminPage ,'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'Checkout.html', context)














    