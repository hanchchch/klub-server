from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import GenericViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(GenericViewSet, ListAPIView, RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
