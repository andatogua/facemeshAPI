from django.db import models
from usuario.models import User
# Create your models here.
class Vehiculo(models.Model):
    num_unidad = models.CharField(max_length=4)
    placa = models.CharField(max_length=7)
    descripcion = models.TextField()
    conductor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.placa