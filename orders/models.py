from django.db import models
from django.contrib.auth import User

# Create your models here.

class Pizza(models.Model):
    name = models.CharField()
    price_medium_size = models.FloatField()
    price_large_size = models.FloatField()
    image = models.ImageField()

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    address = models.CharField()
    is_done = models.BooleanField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=False)
    size = models.CharField(max_length=1)