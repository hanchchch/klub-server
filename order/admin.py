from django.contrib import admin
from .models import Order, Orderer


class OrderAdmin(admin.ModelAdmin):
    list_display = ["orderer", "total", "created_time", "order"]
    search_fields = ["order", "orderer__username"]

admin.site.register(Order, OrderAdmin)

class OrderInlineAdmin(admin.TabularInline):
    model = Order


class OrdererAdmin(admin.ModelAdmin):
    list_display = ["username", "phone", "address"]
    search_fields = ["username", "phone", "address"]

    inlines = [
        OrderInlineAdmin,
    ]

admin.site.register(Orderer, OrdererAdmin)
