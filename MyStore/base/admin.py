from django.contrib import admin

# Register your models here.

from .models import Admins , product



admin.site.register(Admins)
admin.site.register(product)
