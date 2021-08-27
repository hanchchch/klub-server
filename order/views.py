from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.viewsets import GenericViewSet

from .models import Order, Orderer
from .serializers import OrderSerializer, OrdererCreateSerializer, OrdererSerializer


class OrderViewSet(GenericViewSet, CreateAPIView, RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrdererViewSet(GenericViewSet, CreateAPIView, RetrieveAPIView):
    queryset = Orderer.objects.all()
    lookup_field = "phone"
    serializer_class = OrdererSerializer
    serializer_classes = {
        "create": OrdererCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)