from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime


# Create your models here.


class Admins(models.Model):
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    phonenumber = models.CharField(max_length=10)
    storename = models.CharField(max_length=10)
    category= models.CharField(max_length=50)
    storecolor=models.CharField(max_length=10)
    StoreTextColor=models.CharField(max_length=10)
    StoreBackgroundColor= models.CharField(max_length=10)
    totalprice=models.DecimalField(max_digits=10 , decimal_places=2, default=0)
    slug = models.SlugField(blank=True , null=True)

    def __str__(self) :
        return  self.username

    def save(self , *args ,**kwargs):
        if not self.slug :
            self.slug = slugify(self.username)
        super(Admins ,self).save(*args ,**kwargs)


class product(models.Model):
     Admins = models.ForeignKey(Admins, on_delete=models.CASCADE)
     PRDname = models.CharField(max_length=15)
     PRDnumber = models.IntegerField()
     quantity = models.IntegerField()
     PRDimage = models.FileField(upload_to='images')
     price = models.DecimalField(max_digits=10, decimal_places=2)
     desc = models.CharField(max_length=100)
     def __unicode__(self):
        return self.price
     def __str__(self) :
        return  self.PRDname
     def __unicode__(self):
        return self.PRDnumber
     def getprice(self):
        return self.price  
     def deleteProduct(self):
       return self.PRDnumber
     @property
     def image_url(self):
        return self.PRDimage.url
	
class Users(models.Model):
	Name= models.CharField(max_length=15)
	Email=models.CharField(max_length=50)
	password = models.CharField(max_length=15)
	Phonenumber= models.IntegerField(max_length=10)

	
		
	 


class Customer(models.Model):
	customer = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)


	def __str__(self):
		return self.name



class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.customer)
		
	

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	Product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.Product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	name = models.CharField(max_length=200, null=False)
	Phone = models.CharField(max_length=200, null=False)
	email = models.CharField(max_length=200, null=False)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	def get_Customer_Phone(self):	
		return self.Phone
   
class CompletedOrder(models.Model):
	Customer = models.ForeignKey(ShippingAddress,on_delete=models.CASCADE, null=True)
	Order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
	total = models.DecimalField(max_digits=10, decimal_places=2)
	
	def __str__(self):
		return self.Customer.name
	
	

#class CompleteOrder(models.Model):
	#items = models.CharField(max_length=200)
            