from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import GenericViewSet

from .models import ListProduct, Quantity
from .serializers import ListProductSerializer, QuantitySerializer


class ProductViewSet(GenericViewSet, ListAPIView, RetrieveAPIView):
    queryset = ListProduct.objects.all()
    serializer_class = ListProductSerializer


class QuantityViewSet(GenericViewSet, ListAPIView, RetrieveAPIView):
    queryset = Quantity.objects.all()
    serializer_class = QuantitySerializer