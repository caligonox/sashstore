# Generated by Django 4.0 on 2023-11-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_stripe_product_price_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="stripe_product_price_id",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
