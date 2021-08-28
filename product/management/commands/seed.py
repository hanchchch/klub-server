from django.core.management.base import BaseCommand
from product.models import Option, OptionValue, ListProduct, Quantity

class Command(BaseCommand):
    def handle(self, *args, **options):
        shirts_size = Option.objects.create(name="T-Shirt Size")
        shirts_color = Option.objects.create(name="T-Shirt Color")
        tumbler_color = Option.objects.create(name="Tumbler Color")
        sticker_option = Option.objects.create(name="Sticker")

        shirts_black = OptionValue.objects.create(option=shirts_color, value="Black")
        shirts_white =  OptionValue.objects.create(option=shirts_color, value="White")

        shirts_m = OptionValue.objects.create(option=shirts_size, value="M")
        shirts_l = OptionValue.objects.create(option=shirts_size, value="L")
        shirts_xl = OptionValue.objects.create(option=shirts_size, value="XL")

        tumbler_black = OptionValue.objects.create(option=tumbler_color, value="Black")
        tumbler_white = OptionValue.objects.create(option=tumbler_color, value="Pink")

        sticker_fixed = OptionValue.objects.create(option=sticker_option, value="Sticker")

        prod = ListProduct.objects.create(
            name="T-Shirt Black",
            description="Black T-Shirt",
            price=16900,
        )
        prod.options.set([shirts_size])
        prod.fixed_options.set([shirts_black])
        prod.save()


        prod = ListProduct.objects.create(
            name="T-Shirt White",
            description="White T-Shirt",
            price=16900,
        )
        prod.options.set([shirts_size])
        prod.fixed_options.set([shirts_white])
        prod.save()

        prod = ListProduct.objects.create(
            name="Tumbler",
            description="Tumbler",
            price=7900,
        )
        prod.options.set([tumbler_color])
        prod.save()

        prod = ListProduct.objects.create(
            name="Sticker",
            description="Sticker",
            price=5900,
        )
        prod.fixed_options.set([sticker_fixed])
        prod.save()

        prod = ListProduct.objects.create(
            name="Libertas Set",
            description="Libertas Set",
            original_price=22800,
            price=20800,
        )
        prod.options.set([shirts_size, shirts_color])
        prod.fixed_options.set([sticker_fixed])
        prod.save()

        prod = ListProduct.objects.create(
            name="Justitia Set",
            description="Justitia Set",
            original_price=24800,
            price=22800,
        )
        prod.options.set([shirts_size, shirts_color, tumbler_color])
        prod.save()

        prod = ListProduct.objects.create(
            name="Veritas Set",
            description="Justitia Set",
            original_price=13800,
            price=11800,
        )
        prod.options.set([tumbler_color])
        prod.fixed_options.set([sticker_fixed])
        prod.save()

        prod = ListProduct.objects.create(
            name="Young-Tiger Set",
            description="Young-Tiger Set",
            original_price=30700,
            price=27700,
        )
        prod.options.set([shirts_size, shirts_color, tumbler_color])
        prod.fixed_options.set([sticker_fixed])
        prod.save()

        q = Quantity.objects.create(
            quantity=10,
        )
        q.values.set([shirts_m, shirts_black])
        q.save()

        q = Quantity.objects.create(
            quantity=10,
        )
        q.values.set([shirts_l, shirts_black])
        q.save()

        q = Quantity.objects.create(
            quantity=10,
        )
        q.values.set([shirts_xl, shirts_black])
        q.save()

        q = Quantity.objects.create(
            quantity=10,
        )
        q.values.set([shirts_m, shirts_white])
        q.save()

        q = Quantity.objects.create(
            quantity=10,
        )
        q.values.set([shirts_l, shirts_white])
        q.save()

        q = Quantity.objects.create(
            quantity=10,
        )
        q.values.set([shirts_xl, shirts_white])
        q.save()

        q = Quantity.objects.create(
            quantity=10,
        )
        q.values.set([tumbler_black])
        q.save()

        q = Quantity.objects.create(
            quantity=10,
        )
        q.values.set([tumbler_white])
        q.save()

        q = Quantity.objects.create(
            quantity=10,
        )
        q.values.set([sticker_fixed])
        q.save()
