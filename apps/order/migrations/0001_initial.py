# Generated by Django 5.1.4 on 2024-12-19 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 12, 19, 17, 28, 8, 2890)
                    ),
                ),
                ("is_payed", models.BooleanField(default=False)),
                ("total_price", models.BigIntegerField(null=True)),
                ("cart", models.ManyToManyField(to="cart.cartmodel")),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
