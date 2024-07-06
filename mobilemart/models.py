from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, RegexValidator
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .enumeraciones import *
from django.core.exceptions import ValidationError
import re

# Create your models here.
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

def validar_rut(rut):
    if not re.match(r'^\d{7,8}-[\dkK]$', rut):
        raise ValidationError('El formato del RUT no es válido.')

def validar_telefono(telefono):
    if not re.match(r'^\d{9}$', telefono):
        raise ValidationError('El número de teléfono debe contener exactamente 9 dígitos.')


class CustomUser(AbstractBaseUser, PermissionsMixin):
    rut=models.CharField(max_length=12, validators=[validar_rut])
    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(3, message=("El nombre debe tener al menos 3 caracteres"))])
    apellido = models.CharField(max_length=50,  validators=[MinLengthValidator(3, message=("El apellido debe tener al menos 3 caracteres"))])
    email = models.EmailField(unique=True)
    username=models.CharField("Nombre de usuario", max_length=50, validators=[MinLengthValidator(3, message=("El nombre de usuario debe tener al menos 3 caracteres"))])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    telefono = models.CharField(verbose_name="Teléfono", max_length=10, validators=[RegexValidator(r'^\d{9}$', 'El teléfono debe contener exactamente 9 números.')])
    region = models.CharField(verbose_name="Región", max_length=100)  # Nuevo campo
    comuna = models.CharField(max_length=100)  # Nuevo campo
    direccion = models.CharField(verbose_name="Dirección",max_length=255)  # Nuevo campo
    num_departamento = models.CharField(verbose_name="N° de departamento (si aplica)", max_length=10, blank=True)  # Nuevo campo

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return self.email

'''class Usuario(models.Model):
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
        return f"{self.rut}"'''
    

class Celular(models.Model):
    modelo=models.CharField(max_length=50, null=False)
    marca=models.CharField(max_length=20, null=False, choices=MARCA)
    precio=models.IntegerField(default=0, validators=[MinValueValidator(0)])
    especificaciones=models.CharField(max_length=500, null=False)
    foto=models.ImageField(upload_to='celulares', null=True)

    def __str__(self):
        return f"{self.modelo}"

class Carrito(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    celulares = models.ManyToManyField(Celular, through='ItemCarrito')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    celular = models.ForeignKey(Celular, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.celular.modelo} x {self.cantidad}"

    def subtotal(self):
        return self.celular.precio * self.cantidad
    
class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    estado = models.CharField(max_length=20, choices=ESTADO_PEDIDO, default='Pendiente')

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.email}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    celular = models.ForeignKey(Celular, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Detalle del Pedido {self.pedido.id} - {self.celular.modelo}"