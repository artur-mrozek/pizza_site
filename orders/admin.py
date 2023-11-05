from django.contrib import admin
from .models import Pizza, Order, OrderItem


# Register your models here.
admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(OrderItem)