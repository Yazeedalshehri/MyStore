from django.contrib import admin

# Register your models here.

from .models import Admins , product , order, customer, Cart



admin.site.register(Admins)
admin.site.register(product)
admin.site.register(order)
admin.site.register(customer)
admin.site.register(Cart)