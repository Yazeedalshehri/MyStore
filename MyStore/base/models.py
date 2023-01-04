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
     PRDimage = models.ImageField(upload_to='images',null=True )
     price = models.DecimalField(max_digits=10, decimal_places=2)
     desc = models.CharField(max_length=100)

     def __str__(self) :
        return  self.PRDname
