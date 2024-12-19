from rest_framework import serializers
from apps.cart.api.serializers import BaseCartSerializer


class BaseOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cart = BaseCartSerializer(many=True)
    created_at = serializers.DateTimeField()
    is_payed = serializers.BooleanField()
    total_price = serializers.IntegerField()
