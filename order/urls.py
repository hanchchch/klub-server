from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("order", views.OrderViewSet)
router.register("orderer", views.OrdererViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
