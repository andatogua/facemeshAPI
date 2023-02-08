
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import DetalleUsuario

urlpatterns = [
    path('usuario/detalle/', DetalleUsuario.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)