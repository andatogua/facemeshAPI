from dataclasses import fields
from rest_framework import serializers
from .models import Deteccion, Parametro

class DeteccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deteccion
        fields='__all__'

class ParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametro
        fields='__all__'