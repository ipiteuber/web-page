from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Role, UserRole, Product, Coach, CartItem

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'assigned_at')
    search_fields = ('user__username', 'role__role_name')


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('fullname', 'idnumber', 'phone', 'datebirth')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Dates', {'fields': ('last_login',)}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(Product)
admin.site.register(Coach)
admin.site.register(CartItem)
