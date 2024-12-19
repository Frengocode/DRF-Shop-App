from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.product.models import ProductModel


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="media/user/pictures/")
    phone_number = models.CharField(max_length=50)
    products = models.ManyToManyField(ProductModel)
