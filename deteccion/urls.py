
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CrearDeteccion,ListarParametros

urlpatterns = [
    path('deteccion/crear/', CrearDeteccion.as_view()),
    path('deteccion/parametro/listar/', ListarParametros.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)