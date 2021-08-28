from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("product", views.ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("quantity", views.QuantityView.as_view())
]
