from django.contrib import admin
from apps.accounts.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('phone', 'full_name', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    filter_horizontal = ('groups', 'user_permissions') 
    fieldsets = (
        (None, {'fields': ('phone', 'password')}), 
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    
    readonly_fields = ('date_joined',)
    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('phone',) 
