from django.db import models
from django.conf import settings
from datetime import datetime


class Category(models.TextChoices):
    TEXNIK = "Техника", "Техника"
    CAR = "Машина", "Машина"
    HOUSE = "Дом", "Дом"
    PERFUME = "Парфюм", "Парфюм"
    MEAL = "Еда", "Еда"
    CLOTHE = "Одежда", "Одежда"
    TOY = "Игрушка", "Игрушка"
    OTHER = "Другое", "Другое"


class ProductModel(models.Model):
    product_title = models.CharField(max_length=35)
    price = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.utcnow())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_picture = models.ImageField(upload_to="media/product/pictures/")
    description = models.CharField(max_length=200)
    product_category = models.CharField(choices=Category, max_length=50)
