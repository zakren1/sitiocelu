from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .enumeraciones import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    rut=models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username=models.CharField("Nombre de usuario", max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    telefono = models.CharField(verbose_name="Teléfono", max_length=20)  # Nuevo campo
    region = models.CharField(verbose_name="Región", max_length=100)  # Nuevo campo
    comuna = models.CharField(max_length=100)  # Nuevo campo
    direccion = models.CharField(verbose_name="Dirección",max_length=255)  # Nuevo campo
    num_departamento = models.CharField(verbose_name="N° de departamento (si aplica)", max_length=10, blank=True)  # Nuevo campo

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return self.email

# Create your models here.
class Usuario(models.Model):
    rut=models.CharField(max_length=10, primary_key=True)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)
    username=models.CharField("Nombre de usuario", max_length=50, null=False)
    correo=models.EmailField(verbose_name="E-mail")
    password=models.CharField(max_length=50, null=False)
    telefono = models.CharField(verbose_name="Teléfono", max_length=20, blank=True)  # Nuevo campo
    region = models.CharField(verbose_name="Región", max_length=100, blank=True)  # Nuevo campo
    comuna = models.CharField(max_length=100, blank=True)  # Nuevo campo
    direccion = models.CharField(verbose_name="Dirección",max_length=255, blank=True)  # Nuevo campo
    num_departamento = models.CharField(verbose_name="N° de departamento (si aplica)", max_length=10, blank=True)  # Nuevo campo

    def __str__(self):
        return f"{self.rut}"
    

class Celular(models.Model):
    modelo=models.CharField(max_length=50, null=False)
    marca=models.CharField(max_length=20, null=False, choices=MARCA)
    precio=models.IntegerField(default=0, validators=[MinValueValidator(0)])
    especificaciones=models.CharField(max_length=500, null=False)
    foto=models.ImageField(upload_to='celulares', null=True)

    def __str__(self):
        return f"{self.modelo}"
