# Generated by Django 5.1.1 on 2024-09-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_remove_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=25, verbose_name='Rating'),
            preserve_default=False,
        ),
    ]
