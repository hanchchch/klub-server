from rest_framework import serializers
from .models import Option, OptionValue, Product, Quantity


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = "__all__"


class OptionValueSerializer(serializers.ModelSerializer):
    quantities = QuantitySerializer(read_only=True, many=True)

    class Meta:
        model = OptionValue
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    values = OptionValueSerializer(read_only=True, many=True)

    class Meta:
        model = Option
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    options = OptionSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = "__all__"
