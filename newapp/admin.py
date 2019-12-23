from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import (CustomUserAddForm , CustomUserChangeForm)
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserAddForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email' , 'is_staff')
    list_filter = ('is_staff' , 'email')
    fieldsets = (
        (None, {
            "fields": (
                'email' , 'password'
            ),
        }),
        ('Permissions', {
            'fields': (
                'is_staff','is_active'
            )
        })
    )
    add_fieldsets = (
        (None,{
            'classes' :('wide',),
            'fields':(
                'email', 'password1','password2','is_active','is_staff'
            )
        }),
    )
    ordering = ('email',)
    search_fields = ('email',)


admin.site.register(CustomUser , CustomUserAdmin)    
