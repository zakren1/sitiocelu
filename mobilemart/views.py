from django.shortcuts import render, redirect, get_object_or_404
from .models import Celular, CustomUser
from .forms import CelularForm, UpdateCelularForm
from .forms import CustomUserCreationForm, CustomUserUpdateForm, CustomAuthenticationForm
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

class RegistroView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'

def index(request):
    destacado_apple = Celular.objects.filter(marca="Apple").first()
    destacado_samsung = Celular.objects.filter(marca="Samsung").first()
    destacado_xiaomi = Celular.objects.filter(marca="Xiaomi").first()

    datos = {
        "destacado_apple": destacado_apple,
        "destacado_samsung": destacado_samsung,
        "destacado_xiaomi": destacado_xiaomi,
    }
    return render(request,'mobilemart/index.html', datos)

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
def detalle_producto(request, id):
    celular = get_object_or_404(Celular, id=id)

    datos={
        "celular":celular
    }
    return render(request, 'mobilemart/detalleproducto.html', datos)

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
        form = UpdateCelularForm(data=request.POST, files=request.FILES, instance=celular)
        if form.is_valid():
            form.save()
            return redirect('administracion')
        
    datos={
        "form":form,
        "celular":celular
    }
    return render(request, 'mobilemart/ventanaedicion.html', datos)

# Vista para la página crear usuario
def crearusuario(request): 
    form=CustomUserUpdateForm()
    if request.method == 'POST':
        
        form=CustomUserUpdateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="listadousuarios")
            #Redirigir

    datos={
        "form":form
    }
    return render(request, 'mobilemart/crearusuario.html', datos)

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listadousuarios')
    
    datos={
        "usuario":usuario
    }
    return render(request, 'mobilemart/listadousuarios.html', datos)

# Vista para la página listado usuarios
def listadousuarios(request):
    usuarios=CustomUser.objects.all()
    
    datos={
        "usuarios":usuarios
    }
    return render(request, 'mobilemart/listadousuarios.html', datos)

# Vista para la página detalle-modificar usuario
def detalleusuario(request, pk):
    usuario = get_object_or_404(CustomUser, pk=pk)
    form = CustomUserUpdateForm(instance=usuario)

    if request.method == "POST":
        form = CustomUserUpdateForm(data=request.POST, instance=usuario)
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



