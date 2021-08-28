from rest_framework import serializers
from .models import Option, OptionValue, ListProduct, Quantity


class OptionValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionValue
        fields = ["id", "value", "option"]


class QuantitySerializer(serializers.ModelSerializer):
    values = OptionValueSerializer(read_only=True, many=True)

    class Meta:
        model = Quantity
        fields = "__all__"


class OptionSerializer(serializers.ModelSerializer):
    values = OptionValueSerializer(read_only=True, many=True)

    class Meta:
        model = Option
        fields = '__all__'


class ListProductSerializer(serializers.ModelSerializer):
    options = OptionSerializer(read_only=True, many=True)
    fixed_options = OptionValueSerializer(read_only=True, many=True)

    class Meta:
        model = ListProduct
        fields = "__all__"
