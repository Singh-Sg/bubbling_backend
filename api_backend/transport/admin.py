from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import Users
from .models import (
    Manufacturer,
    Car,
)



class UsersUserAdmin(UserAdmin):
    model = Users
    list_display = ('email', 'is_staff', 'is_active', 'first_name', 'last_name')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),

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
    readonly_fields = ('email',)


class ManufacturerAdmin(admin.ModelAdmin):    
      list_per_page = 5
      list_display = ["id","name", "country", "created_at", "updated_at"]



admin.site.register(Users, UsersUserAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car)

