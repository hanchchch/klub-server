from django.db import models

class Orderer(models.Model):
    username = models.CharField(max_length=32)
    phone = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=256)
    donation = models.CharField(max_length=256, blank=True)

class Order(models.Model):
    order = models.CharField(max_length=512)
    total = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.DateTimeField(null=True)
    orderer = models.ForeignKey(Orderer, on_delete=models.CASCADE, related_name="orders")
