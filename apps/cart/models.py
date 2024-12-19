from django.db import models
from django.conf import settings
from datetime import datetime
from apps.product.models import ProductModel


class CartModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.utcnow())
    is_ready_to_order = models.BooleanField(default=False)
    quantity = models.BigIntegerField(default=1)
    total_price = models.BigIntegerField(null=True)

    class Meta:
        ordering = ["-created_at"]
