from django.db import models
from apps.base.models import BaseModel
from mptt.models import MPTTModel, TreeForeignKey
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
    title = RichTextField()
    image = models.ImageField(upload_to='banner_image/', verbose_name="Banner image")
    url = models.URLField(verbose_name="Banner url")


    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
    
    def __str__(self):
        return f"{self.id}"


