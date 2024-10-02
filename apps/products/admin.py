from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from apps.products.models import (
    Category, 
    Banner,
    Brand,
    Tag,
    Color,
    Size,
    Product,
    ProductImage,
    ProductSize,
    AdditionalInfo,
    Review,
    Service
)

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'created_at', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('indented_title',)
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    list_per_page = 20
    sortable_by = ['created_at']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ( 'review', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 0

class AdditionalInfoInline(admin.TabularInline):
    model = AdditionalInfo
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'brand', 'SKU')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    filter_horizontal = ('tags', 'category')
    inlines = [
        ProductImageInline,
        ProductSizeInline,
        AdditionalInfoInline
    ]



