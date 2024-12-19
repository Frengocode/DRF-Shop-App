# Generated by Django 5.1.4 on 2024-12-19 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CartModel",
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
                        default=datetime.datetime(2024, 12, 19, 17, 28, 8, 632)
                    ),
                ),
                ("is_ready_to_order", models.BooleanField(default=False)),
                ("quantity", models.BigIntegerField(default=1)),
                ("total_price", models.BigIntegerField(null=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
