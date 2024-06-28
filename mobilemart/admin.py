from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Celular, CustomUser, Pedido

class AdmCustomUser(UserAdmin):
    model = CustomUser
    list_display = ('email', 'nombre', 'apellido', 'rut','is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido', 'rut', 'telefono', 'region', 'comuna', 'direccion')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'nombre', 'apellido', 'rut')
    ordering = ('email',)

#class AdmUsuario(admin.ModelAdmin):
    #list_display= ['rut', 'nombre', 'apellido', 'username', 'correo']
    #list_editable= ['rut', 'username', 'correo']

class AdmCelular(admin.ModelAdmin):
    list_display=['marca', 'modelo', 'precio', 'foto'] #El id lo creó Django autom. por que Mascota no tiene clave primaria
    list_editable=['precio', 'foto']
    list_filter=['marca']

class AdmPedido(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'total', 'estado', 'fecha_pedido']
    list_filter = ['estado', 'fecha_pedido']
    search_fields = ['usuario__email', 'id']
    ordering = ['fecha_pedido']



# Register your models here.
#admin.site.register(Usuario, AdmUsuario)
admin.site.register(Celular, AdmCelular)
admin.site.register(CustomUser, AdmCustomUser)
admin.site.register(Pedido, AdmPedido)
