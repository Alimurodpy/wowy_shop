from django.db import models
from apps.base.models import BaseModel
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

class Category(BaseModel, MPTTModel):
    title = models.CharField(max_length=255, verbose_name="Category name")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    icon = models.CharField( max_length=255, null=True, blank=True, verbose_name="Icon")
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

class Service(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Service title")
    icon = models.FileField(upload_to='service_icon/', verbose_name="Service icon")
    description = models.TextField(verbose_name="Service description")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title

class Brand(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Brand name")
    logo = models.ImageField(upload_to='brand_logo/', verbose_name="Brand logo")

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.title

class Tag(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Tag name")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

class Color(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Color name")
    code = models.CharField(max_length=255, verbose_name="Color code")

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return self.name

class Size(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Size name")

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self):
        return self.name 

class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Product title")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name="Brand")
    category = models.ManyToManyField('Category', verbose_name="Category")
    short_desc = models.TextField(verbose_name="Short description")
    description = RichTextField()
    SKU = models.CharField(max_length=100, verbose_name="SKU")
    tags = models.ManyToManyField('Tag', verbose_name="Tags")


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

class ProductImage(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product", related_name="images")
    color = models.ForeignKey('Color', on_delete=models.CASCADE, verbose_name="Color")
    image = models.ImageField(upload_to='product_image/', verbose_name="Product image")


    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"

    def __str__(self):
        return self.product.title

class ProductSize(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product")
    color = models.ForeignKey('Color', on_delete=models.CASCADE, verbose_name="Color")
    size = models.ForeignKey('Size', on_delete=models.CASCADE, verbose_name="Size")
    availability = models.IntegerField(default=True, verbose_name="Availability")
    price = models.FloatField(verbose_name="Price")

# class Attribute(BaseModel):
#     product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product")
#     name = models.CharField(max_length=255, verbose_name="Attribute name")

# class AttributeValue(BaseModel):
#     attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE, verbose_name="Attribute")
#     value = models.CharField(max_length=255, verbose_name="Attribute value")


class AdditionalInfo(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product")
    key = models.CharField(max_length=255, verbose_name="Key")
    value = models.CharField(max_length=255, verbose_name="Value")

    class Meta:
        verbose_name = "Additional info"
        verbose_name_plural = "Additional infos"

    def __str__(self):
        return self.key
    
class Review(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product")
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name="User")
    review = models.TextField(verbose_name="Text")
    rating = models.IntegerField(verbose_name="Rate")

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.product.title