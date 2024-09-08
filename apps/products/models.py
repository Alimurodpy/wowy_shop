from django.db import models
from apps.base.models import BaseModel
from mptt.models import MPTTModel, TreeForeignKey
#import RichTextField
from ckeditor.fields import RichTextField

class Category(BaseModel, MPTTModel):
    title = models.CharField(max_length=255, verbose_name="Category name")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    icon = models.TextField(null=True, blank=True, verbose_name="Icon")
    photo = models.ImageField(upload_to='category_photo/', null=True, blank=True , verbose_name="Category photo")

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['title']
    def __str__(self):
        return self.title

class Banner(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Banner title")
    photo = models.ImageField(upload_to='banner_photo/', verbose_name="Banner photo")
    body = RichTextField()
    

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.title
