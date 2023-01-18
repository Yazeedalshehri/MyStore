from django.db import models
from django.utils.text import slugify

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
     PRDimage = models.ImageField(upload_to='images')
     price = models.DecimalField(max_digits=10, decimal_places=2)
     desc = models.CharField(max_length=100)
     def __unicode__(self):
        return self.price
     def __str__(self) :
        return  self.PRDname


class order(models.Model):
    orNumber = models.CharField(max_length=15)
    Admins = models.ForeignKey(Admins, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(product) 
    status = models.CharField(max_length=15)
    def __str__(self) :
        return  self.Admins.username+self.orNumber
    def getprice(self):
        return self.total 

    

class User(models.Model):
     Name = models.CharField(max_length=15)
     Email = models.CharField(max_length=30)
     password = models.CharField(max_length=15)
     Phonenumber = models.CharField(max_length=10)
     def __str__(self) :
        return  self.Name


class Cart(models.Model):
     Admin = models.CharField(max_length=15) 
     User = models.CharField(max_length=15)
     Product=models.CharField(max_length=15)
     Total=models.DecimalField(max_digits=10, decimal_places=2)
     def __str__(self) :
        return  self.product
   

                