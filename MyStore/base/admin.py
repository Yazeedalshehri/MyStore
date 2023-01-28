from django.contrib import admin

# Register your models here.

from .models import Admins , product , Order, Customer,OrderItem,CompletedOrder,ShippingAddress



admin.site.register(Admins)
admin.site.register(product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(CompletedOrder)
admin.site.register(ShippingAddress)