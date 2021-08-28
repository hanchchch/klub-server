from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import ListProduct, Quantity
from .serializers import ListProductSerializer, QuantitySerializer


class ProductViewSet(GenericViewSet, ListAPIView, RetrieveAPIView):
    queryset = ListProduct.objects.all()
    serializer_class = ListProductSerializer


class QuantityView(GenericAPIView):
    queryset = Quantity.objects.all()
    serializer_class = QuantitySerializer

    def post(self, request, *args, **kwargs):
        options = request.data.get("options", [])
        is_set = request.data.get("is_set", False)
        qs = self.get_queryset()

        if not is_set:
            for option in options:
                qs = qs.filter(values__id__in=[option["id"]])
            return Response(self.get_serializer(qs, many=True).data)
            
        else:
            result = []
            print(qs)
            for option in options:
                qs = qs.filter(values__id__in=[option["id"]])
                print(qs)
                if qs.count() == 1:
                    result.append(self.get_serializer(qs.first()).data)
                    qs = self.get_queryset()
                
            return Response(result)
