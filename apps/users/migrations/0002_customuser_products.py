# Generated by Django 5.1.4 on 2024-12-19 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0007_alter_productmodel_created_at"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="products",
            field=models.ManyToManyField(to="product.productmodel"),
        ),
    ]
