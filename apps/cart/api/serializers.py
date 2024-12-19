from rest_framework import serializers
from apps.product.api.serializers import BaseProductSerializers


class BaseCartSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    product = BaseProductSerializers()
    created_at = serializers.DateTimeField()
    quantity = serializers.IntegerField()
    total_price = serializers.IntegerField()
