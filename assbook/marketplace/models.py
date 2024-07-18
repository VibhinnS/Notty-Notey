from django.db import models
from typing import TypeAlias
from datetime import datetime

date: TypeAlias = datetime
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name :str = models.CharField(max_length=255)
    phone :str = models.CharField(max_length=255)
    email :str = models.CharField(max_length=255)
    date_purchased :date = models.DateTimeField(auto_now_add=True)
    tag :str = models.OneToOneField(Tag, on_delete=models.SET_NULL, null=True)

class Product(models.Model):
    CATEGORIES = (
        ('Decor', 'Decor'),
        ('Personal Care', 'Personal Care'),
        ('Pets', 'Pets')
    )
    product_id :int = models.IntegerField()
    name :str = models.CharField(max_length=255)
    price :float = models.FloatField()
    category :str = models.CharField(max_length=255, null=True, choices=CATEGORIES)
    description :str = models.CharField(max_length=1000)
    date_created :date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', "out for Delivery"),
        ('Delivered', 'Devlievered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_of_order_placement :date = models.DateTimeField(auto_now_add=True)
    status :str = models.CharField(max_length=200, null=True, choices=STATUS)
    tag :str = models.OneToOneField(Tag, on_delete=models.SET_NULL, null=True)
