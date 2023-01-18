from django.contrib import admin

# Register your models here.

from .models import Admins , product , order, User, Cart



admin.site.register(Admins)
admin.site.register(product)
admin.site.register(order)
admin.site.register(User)
admin.site.register(Cart)