from django.db import models
from django.conf import settings
from apps.cart.models import CartModel
from datetime import datetime


class OrderModel(models.Model):
    cart = models.ManyToManyField(CartModel)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.utcnow())
    is_payed = models.BooleanField(default=False)
    total_price = models.BigIntegerField(null=True)

    class Meta:
        ordering = ["-created_at"]
