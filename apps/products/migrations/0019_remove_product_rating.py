# Generated by Django 5.1.1 on 2024-09-29 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
