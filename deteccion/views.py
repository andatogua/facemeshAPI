from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .models import Deteccion, Parametro
from .serializers import DeteccionSerializer, ParametroSerializer

class CrearDeteccion(generics.CreateAPIView):
    permission_classes =[IsAuthenticated,IsAdminUser]
    authentication_classes = (TokenAuthentication,)
    queryset = Deteccion.objects.all()
    serializer_class = DeteccionSerializer

class ListarParametros(generics.ListAPIView):
    permission_classes =[IsAuthenticated,IsAdminUser]
    authentication_classes = (TokenAuthentication,)
    queryset = Parametro.objects.all()
    serializer_class = ParametroSerializer