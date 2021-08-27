from rest_framework import serializers
from .models import Order, Orderer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrdererCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderer
        fields = "__all__"

class OrdererSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Orderer
        fields = "__all__"
