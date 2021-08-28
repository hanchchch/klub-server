from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/order/", include("order.urls")),
    path("api/product/", include("product.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
