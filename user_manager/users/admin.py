from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users

class UsersUserAdmin(UserAdmin):
    model = Users
    list_display = ('email', 'is_staff', 'is_active', 'first_name', 'last_name')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', "api_backend_token")}),

        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', "user_permissions")}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'first_name', 'last_name')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Users, UsersUserAdmin)
