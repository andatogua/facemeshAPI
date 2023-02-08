from django.contrib import admin
from .models import Deteccion, Parametro

# Register your models here.
admin.site.register(Parametro)
admin.site.register(Deteccion)