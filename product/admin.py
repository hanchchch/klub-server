from django.contrib import admin
from .models import OptionValue, ListProduct, Quantity, Option


class QuantityAdmin(admin.ModelAdmin):
    model = Quantity


class OptionValuesInlineAdmin(admin.TabularInline):
    model = OptionValue


class OptionsAdmin(admin.ModelAdmin):
    inlines = [
        OptionValuesInlineAdmin,
    ]


class OptionsInlineAdmin(admin.TabularInline):
    model = ListProduct.options.through


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        OptionsInlineAdmin,
    ]

admin.site.register(Option, OptionsAdmin)
admin.site.register(Quantity, QuantityAdmin)
admin.site.register(ListProduct, ProductAdmin)