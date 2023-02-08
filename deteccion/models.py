from django.db import models
from usuario.models import User

# Create your models here.
class Parametro(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.nombre

class Deteccion(models.Model):
    parametro = models.ForeignKey(Parametro, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)
    conductor = models.ForeignKey(User, on_delete=models.CASCADE)
    num_detecciones = models.IntegerField(max_length=3)

    def __str__(self) -> str:
        return str(self.conductor)