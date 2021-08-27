from product.models import Quantity
from django.db import models

class Orderer(models.Model):
    username = models.CharField(max_length=32)
    phone = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=256)
    donation = models.CharField(max_length=256, blank=True)

    def __str__(self) -> str:
        return f"{self.username} ({self.phone})"


class Order(models.Model):
    order = models.ForeignKey(Quantity, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.DateTimeField(null=True)
    orderer = models.ForeignKey(Orderer, on_delete=models.CASCADE, related_name="orders")

    def __str__(self) -> str:
        return f"{self.orderer} {self.total}"
