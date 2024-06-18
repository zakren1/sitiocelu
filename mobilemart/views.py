from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Usuario, Celular
from .forms import UsuarioForm, UpdateUsuarioForm, CelularForm, UpdateCelularForm
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request,'mobilemart/index.html')

# Vista para la página de Samsung
def samsung(request):
    celulares = Celular.objects.filter(marca="Samsung")
    datos = {"celulares": celulares}
    return render(request, 'mobilemart/samsung.html', datos)

# Vista para la página de Xiaomi
def xiaomi(request):
    celulares = Celular.objects.filter(marca="Xiaomi")
    datos = {"celulares": celulares}
    return render(request, 'mobilemart/xiaomi.html', datos)

# Vista para la página de Apple
def iphone(request):
    celulares = Celular.objects.filter(marca="Apple")
    datos = {"celulares": celulares}
    return render(request, 'mobilemart/iphone.html', datos)

# Vista para la página del Carrito
def carrito(request):
    return render(request, 'mobilemart/carrito.html')

# Vista para la página del Perfil del Usuario
def perfilusuario(request):
    return render(request, 'mobilemart/perfilusuario.html')

# Vista para la página de Pedidos del Usuario
def pedidosuser(request):
    return render(request, 'mobilemart/pedidosuser.html')

# Vista para la página de Inicio de Sesión
#def iniciosesion(request):
#    return render(request, 'registration/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect(to='index')

# Vista para la página Acerca de
def about(request):
    return render(request, 'mobilemart/about.html')

# Vista para la página detalle producto
def detalle_producto(request):
    return render(request, 'mobilemart/pa-iphone15pro.html')

# Vista para la página recuperar contraseña
def recuperar_contrasena(request):
    return render(request, 'mobilemart/recuperarcontra.html')

# Vista para la página registro usuario
def registro_usuario(request):
    return render(request, 'registration/registro.html')

# Vista para la página detalle pedido usuario
def detalle_pedido_usuario(request):
    return render(request, 'mobilemart/detallepedidouser.html')

##### VISTAS DE ADMINISTRADOR #####

# Vista para la página de Administración (editarproducto)
def administracion(request):

    celulares=Celular.objects.all() #queryset
    
    datos={
        "celulares":celulares
    }
    return render(request, 'mobilemart/editarproducto.html', datos)

# Vista para la página agregar producto
def agregarproducto(request):

    form=CelularForm()
    if request.method == 'POST':
        
        form=CelularForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="administracion")
            #Redirigir

    datos={
        "form":form
    }
    return render(request, 'mobilemart/agregarproducto.html', datos)

def eliminar_producto(request, id):
    celular = get_object_or_404(Celular, id=id)
    if request.method == 'POST':
        remove(path.join(str(settings.MEDIA_ROOT).replace('/media',''))+celular.foto.url)
        celular.delete()
        return redirect('administracion')
    
    datos={
        "celulares":celular
    }
    return render(request, 'mobilemart/eliminarproducto.html', datos)

# Vista para la página ventana edición (editar producto específico)
def ventanaedicion(request, id):
    celular = get_object_or_404(Celular, id=id)
    form = UpdateCelularForm(instance=celular)

    if request.method == "POST":
        form = UpdateCelularForm(data=request.POST, instance=celular)
        if form.is_valid():
            form.save()
            return redirect('administracion')
        
    datos={
        "form":form,
        "ceular":celular
    }
    return render(request, 'mobilemart/ventanaedicion.html', datos)

# Vista para la página crear usuario
def crearusuario(request):
    
    form=UsuarioForm()
    if request.method == 'POST':
        
        form=UsuarioForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="listadousuarios")
            #Redirigir

    datos={
        "form":form
    }
    return render(request, 'mobilemart/crearusuario.html', datos)

def eliminar_usuario(request, rut):
    usuario = get_object_or_404(Usuario, rut=rut)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listadousuarios')
    
    datos={
        "usuarios":usuario
    }
    return render(request, 'mobilemart/listadousuarios.html', datos)

# Vista para la página listado usuarios
def listadousuarios(request):
    usuarios=Usuario.objects.all()
    
    datos={
        "usuarios":usuarios
    }
    return render(request, 'mobilemart/listadousuarios.html', datos)

# Vista para la página detalle-modificar usuario
def detalleusuario(request, rut):
    usuario = get_object_or_404(Usuario, rut=rut)
    form = UpdateUsuarioForm(instance=usuario)

    if request.method == "POST":
        form = UpdateUsuarioForm(data=request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listadousuarios')
        
    datos={
        "form":form,
        "usuario":usuario
    }
    
    return render(request, 'mobilemart/detalleusuario.html',datos)

# Vista para la página listado pedidos
def listadopedidos(request):
    return render(request, 'mobilemart/listadopedidos.html')

# Vista para la página detalle pedido
def detallepedido(request):
    return render(request, 'mobilemart/detallepedido.html')



