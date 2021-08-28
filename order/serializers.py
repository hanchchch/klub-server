from django.conf import settings
from rest_framework import serializers
from .models import Order, Orderer

from slack_sdk.webhook import WebhookClient

url = settings.SLACK_WEBHOOK_URL
webhook = WebhookClient(url)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        order = validated_data.get("order")
        total = validated_data.get("total")
        orderer = validated_data.get("orderer")
        webhook.send(
            blocks=[
                {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"{orderer.username}님 주문정보",
                },
                },
                { "type": "divider" },
                {
                "type": "section",
                "fields": [
                    {
                    "type": "mrkdwn",
                    "text": f"\n>*{orderer.username}*\n>{orderer.phone}\n>{orderer.address}\n>{orderer.donation}"
                    },
                    {
                    "type": "mrkdwn",
                    "text": order
                    },
                ],
                },
                {
                "type": "divider",
                },
                {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"총 금액: *₩{total}*",
                },
                },
            ],
        )
        targets = validated_data.pop("target")
        for target in targets:
            target.quantity = target.quantity - 1
            target.save()
        order = Order.objects.create(**validated_data)
        order.target.set(targets)
        order.save()
        return order

class OrdererCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderer
        fields = "__all__"

class OrdererSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Orderer
        fields = "__all__"
