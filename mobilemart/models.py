from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .enumeraciones import *


# Create your models here.
class Usuario(models.Model):
    rut=models.CharField(max_length=10, primary_key=True)
    username=models.CharField(max_length=50, null=False)
    correo=models.EmailField(verbose_name="E-mail")
    password=models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.rut}"
    

class Celular(models.Model):
    modelo=models.CharField(max_length=50, null=False)
    marca=models.CharField(max_length=20, null=False, choices=MARCA)
    precio=models.IntegerField(default=0, validators=[MinValueValidator(0)])
    especificaciones=models.CharField(max_length=300, null=False)
    foto=models.ImageField(upload_to='celulares', null=True)

    def __str__(self):
        return f"{self.modelo}"
