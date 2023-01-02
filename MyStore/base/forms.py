from django import forms
from . import models
from django.contrib.auth.models import User


class Admins(forms.ModelForm):
    class Meta:
        model = models.Admins
        fields = ['username','email','password','phonenumber']