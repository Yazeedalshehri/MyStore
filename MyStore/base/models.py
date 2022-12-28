from django.db import models

# Create your models here.


class Admins(models.Model):
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=17)
    phonenumber = models.IntegerField()
