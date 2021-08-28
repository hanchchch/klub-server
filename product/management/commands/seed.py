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
            description="심플한 무드의 KU 로고 프린팅 티셔츠\n크림슨 색배합과 캠퍼스 위치가 새겨져있어요.",
            price=16900,
        )
        prod.options.set([shirts_size])
        prod.fixed_options.set([shirts_black])
        prod.save()


        prod = ListProduct.objects.create(
            name="T-Shirt White",
            description="키치한 무드의 KLUB 오리지널 캐릭터 오버핏 티셔츠\n-학교 밖에서도 편하게 입을 수 있어요.",
            price=16900,
        )
        prod.options.set([shirts_size])
        prod.fixed_options.set([shirts_white])
        prod.save()

        prod = ListProduct.objects.create(
            name="Tumbler",
            description="카페, 학교 등에서 가볍게 쓰기 좋은 컴팩트한 사이즈에요.\n분리형 이중 구조로 되어있어 세척, 보온이 용이합니다.",
            price=7900,
        )
        prod.options.set([tumbler_color])
        prod.save()

        prod = ListProduct.objects.create(
            name="Laptop Stickers",
            description="무광 스티커 9종으로 구성된 KLUB의 오리지널 스티커 세트\n노트북, 핸드폰, 노트, 아이패드 등에\n붙이기 적당한 사이즈에요.\nKU의 무드로 주변을 꾸며보세요!",
            price=5900,
        )
        prod.fixed_options.set([sticker_fixed])
        prod.save()

        prod = ListProduct.objects.create(
            name="Libertas Set",
            description="티셔츠 & 스티커\n\n일상에서 소소하게 느낌내기 좋은 세트!",
            original_price=22800,
            price=20800,
        )
        prod.options.set([shirts_size, shirts_color])
        prod.fixed_options.set([sticker_fixed])
        prod.save()

        prod = ListProduct.objects.create(
            name="Justitia Set",
            description="티셔츠 & 텀블러\n\n이번 학기 과탑 예약! 공부할 때 쓰기 좋은 실용성 최고 세트",
            original_price=24800,
            price=22800,
        )
        prod.options.set([shirts_size, shirts_color, tumbler_color])
        prod.save()

        prod = ListProduct.objects.create(
            name="Veritas Set",
            description="스티커 & 텀플러\n\n수험생, 선후배 선물로 제격인 아이템 세트!",
            original_price=13800,
            price=11800,
        )
        prod.options.set([tumbler_color])
        prod.fixed_options.set([sticker_fixed])
        prod.save()

        prod = ListProduct.objects.create(
            name="Young-Tiger Set",
            description="티셔츠 & 스티커 & 텀블러\n\n모든 걸 다 담았다! 한정 판매 아이템들을 놓치기 싫은 당신을 위한 세트",
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
