from django.contrib import admin
from .models import OptionValue, ListProduct, ProductImage, Quantity, Option


class QuantityAdmin(admin.ModelAdmin):
    model = Quantity


class OptionValuesInlineAdmin(admin.TabularInline):
    model = OptionValue


class OptionsAdmin(admin.ModelAdmin):
    inlines = [
        OptionValuesInlineAdmin,
    ]

class ProductOptionInlineAdmin(admin.TabularInline):
    model = ListProduct.options.through

class ProductOptionValueInlineAdmin(admin.TabularInline):
    model = ListProduct.fixed_options.through

class ProductImageInlineAdmin(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInlineAdmin,
        ProductOptionInlineAdmin,
        ProductOptionValueInlineAdmin,
    ]

admin.site.register(Option, OptionsAdmin)
admin.site.register(Quantity, QuantityAdmin)
admin.site.register(ListProduct, ProductAdmin)