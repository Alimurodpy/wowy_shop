# Generated by Django 5.1.1 on 2024-10-02 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255, verbose_name='Advertising title')),
                ('image', models.ImageField(upload_to='advertising_image/', verbose_name='Advertising image')),
                ('url', models.URLField(verbose_name='Advertising url')),
            ],
            options={
                'verbose_name': 'Advertising',
                'verbose_name_plural': 'Advertisings',
            },
        ),
    ]
