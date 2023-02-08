from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('cedula','correo', 'nombre','apellido')}),
    )
    add_fieldsets = (
        (
            'Datos',
            {
                'fields': ('cedula','correo', 'nombre', 'apellido')
            }
        ),
    )
    list_display = ('cedula','nombre','apellido','correo')
    list_filter = ('cedula','apellido')
    search_fields = ('cedula','apellido')
    ordering = ('cedula',)

admin.site.register(User,UserAdmin)