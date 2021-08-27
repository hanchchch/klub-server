from django.db import models

class Order(models.Model):
    username = models.CharField(max_length=32)
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    order = models.CharField(max_length=512)
    total = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.DateTimeField(null=True)
