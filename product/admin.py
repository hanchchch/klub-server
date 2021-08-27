from django.contrib import admin
from .models import OptionValue, Product, Category, Quantity, SetProduct, Option


class QuantityAdmin(admin.ModelAdmin):
    model = Quantity


class OptionValuesInlineAdmin(admin.TabularInline):
    model = OptionValue


class OptionsAdmin(admin.ModelAdmin):
    inlines = [
        OptionValuesInlineAdmin,
    ]


class OptionsInlineAdmin(admin.TabularInline):
    model = Option


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        OptionsInlineAdmin,
    ]

admin.site.register(Category)
# admin.site.register(Option, OptionsAdmin)
admin.site.register(Quantity, QuantityAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SetProduct)