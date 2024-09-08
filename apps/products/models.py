from django.db import models
from apps.base.models import BaseModel

class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Category name")
    icon = models.TextField(null=True, blank=True verbose_name="Icon")
    photo = models.ImageField(upload_to='category_photo/', null=True, blank=True)
     