from django.contrib import admin
from .models import Usuario
from .models import Celular

class AdmUsuario(admin.ModelAdmin):
    list_display= ['rut', 'username', 'correo']
    #list_editable= ['rut', 'username', 'correo']

class AdmCelular(admin.ModelAdmin):
    list_display=['marca', 'modelo', 'precio', 'foto'] #El id lo creó Django autom. por que Mascota no tiene clave primaria
    list_editable=['precio', 'foto']
    list_filter=['marca']




# Register your models here.
admin.site.register(Usuario, AdmUsuario)
admin.site.register(Celular, AdmCelular)

