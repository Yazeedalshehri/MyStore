from django import forms
from . import models
from django.contrib.auth.models import User
from .models import Admins
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username','first_name','last_name','email']




class AdminsForm(forms.ModelForm):
    class Meta:
        model = Admins
        fields = ('phonenumber','storename')

        widgets ={
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'storename': forms.TextInput(attrs={'class': 'form-control'}),
        }