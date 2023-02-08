from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, cedula, correo, nombre, apellido,**extra_fields):
        if not correo:
            raise ValueError("Debe ingresar un correo electronico")
        correo = self.normalize_email(correo)
        usuario = self.model(
            cedula = cedula,
            correo = correo,
            nombre = nombre,
            apellido = apellido,
            **extra_fields
        )
        usuario.set_password(cedula)
        usuario.save(using=self._db)
        return usuario
    
    def create_user(self, cedula, correo,  nombre, apellido,**extra_fields):
        return self._create_user(cedula, correo,  nombre, apellido,**extra_fields)

    def create_superuser(self, cedula, correo,  nombre, apellido,**extra_fields):
        user = self._create_user(cedula, correo,  nombre, apellido,**extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    cedula = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(max_length=254, unique=True)
    nombre = models.CharField(max_length=254, null=True, blank=True)
    apellido = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    USERNAME_FIELD = 'cedula'
    EMAIL_FIELD = 'correo'
    REQUIRED_FIELDS = ['correo','nombre', 'apellido']

    objects = UserManager()

    def get_absolute_url(self):
        return "/user/%i/" % (self.pk)
    
    def __str__(self) -> str:
        return self.cedula