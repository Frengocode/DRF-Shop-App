from rest_framework import serializers
from ..models import Category, ProductModel
from apps.users.api.serializers import UserSerializers

### SEE ALL SERIALZIERS
### ListSerializer


class BaseProductSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    product_title = serializers.CharField()
    price = serializers.IntegerField()
    product_picture = serializers.ImageField()
    description = serializers.CharField()
    product_category = serializers.ChoiceField(choices=Category)
    user = UserSerializers(read_only=True)


class CreateProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            "product_title",
            "price",
            "product_picture",
            "description",
            "product_category",
        ]

    def create(self, validated_data):
        user = self.context["request"].user

        product = ProductModel.objects.create(**validated_data, user=user)

        user.products.add(product)

        return product


class GetProductsSerializers(BaseProductSerializers):
    pass


class GetProductSerializers(BaseProductSerializers):
    pass


class UpdateProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            "product_title",
            "price",
            "product_picture",
            "description",
            "product_category",
        ]
