# Generated by Django 5.1.1 on 2024-09-08 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_banner_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Banner name'),
            preserve_default=False,
        ),
    ]
