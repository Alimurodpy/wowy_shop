from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from apps.products.models import Category

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'created_at', 'is_active')
    list_display_links = ('indented_title',)
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    list_per_page = 20
