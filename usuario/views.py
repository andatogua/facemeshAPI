from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .models import User
from .serializers import UserSerializer

class DetalleUsuario(generics.RetrieveUpdateAPIView):
    permission_classes =[IsAuthenticated,IsAdminUser]
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user