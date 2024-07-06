from django.shortcuts import render, redirect, get_object_or_404
from .models import Celular, CustomUser, Carrito, ItemCarrito, Pedido
from .forms import CelularForm, UpdateCelularForm, ActualizarEstadoPedidoForm
from .forms import CustomUserCreationForm, CustomUserUpdateForm, CustomAuthenticationForm
from os import remove, path
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect
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
        
def redirect_login(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse_lazy('administracion'))
    else:
        return HttpResponseRedirect(reverse_lazy('index'))

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

@login_required
def agregar_al_carrito(request, id):
    celular = get_object_or_404(Celular, id=id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, celular=celular)
    if not created:
        item.cantidad += 1
        item.save()
    
    messages.success(request, 'Producto agregado al carrito')
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()

    total_productos = sum(item.celular.precio * item.cantidad for item in items)
    if total_productos == 0:
        envio = 0
    else:
        envio = 5990
    total = total_productos + envio

    datos = {
        'carrito': carrito,
        'items': items,
        'total_productos': total_productos,
        'total': total,
        'envio': envio
    }
    return render(request, 'mobilemart/carrito.html', datos)

@login_required
def actualizar_carrito(request, id):
    item = get_object_or_404(ItemCarrito, id=id, carrito__usuario=request.user)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'incrementar':
            item.cantidad += 1
            item.save()
            messages.success(request, 'Cantidad incrementada')
        elif action == 'decrementar':
            if item.cantidad > 1:
                item.cantidad -= 1
                item.save()
                messages.success(request, 'Cantidad decrementada')
            else:
                messages.error(request, 'La cantidad no puede ser menor a 1')
    return redirect('ver_carrito')

@login_required
def eliminar_item_carrito(request, id):
    item = get_object_or_404(ItemCarrito, id=id, carrito__usuario=request.user)
    item.delete()
    messages.success(request, 'Producto eliminado del carrito')
    return redirect('ver_carrito')

@login_required
def confirmar_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = ItemCarrito.objects.all()
    total_productos = sum(item.celular.precio * item.cantidad for item in items)
    if total_productos == 0:
        envio = 0
    else:
        envio = 5990
    total = total_productos + envio

    if request.method == 'POST':
            # Crear el pedido
            usuario = request.user
            pedido = Pedido(usuario=usuario, total=total)
            pedido.save()

            # Agregar los productos al pedido
            for item in items:
                detalle_pedido = pedido.detalles.create(
                    celular=item.celular,
                    cantidad=item.cantidad,
                    precio=item.celular.precio * item.cantidad
                )
                detalle_pedido.save()

            # Vaciar el carrito
            ItemCarrito.objects.all().delete()

            messages.success(request, '¡Pago exitoso!')

            return redirect('detalle_pedido_usuario', id=pedido.id)

    return render(request, 'mobilemart/confirmar_carrito.html', {'items': items, 'total': total})

# Vista para la página del Perfil del Usuario
@login_required
def perfilusuario(request):
    if request.method == "POST":
        form = CustomUserUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente')
            return redirect('perfilusuario')
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'mobilemart/perfilusuario.html', {'form': form})

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

@login_required
def pedidosuser(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'mobilemart/pedidosuser.html', {'pedidos': pedidos})


@login_required
def detalle_pedido_usuario(request, id):
    pedido = get_object_or_404(Pedido, id=id, usuario=request.user)
    return render(request, 'mobilemart/detallepedidouser.html', {'pedido': pedido})

##### VISTAS DE ADMINISTRADOR #####

# Vista para la página de Administración (editarproducto)
@user_passes_test(lambda u: u.is_superuser)
def administracion(request):
    celulares=Celular.objects.all() #queryset
    
    datos={
        "celulares":celulares
    }
    return render(request, 'mobilemart/editarproducto.html', datos)

# Vista para la página del Perfil del Usuario del Admin
def perfilusuarioadmin(request):
    if request.method == "POST":
        form = CustomUserUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfilusuarioadmin')
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'mobilemart/perfilusuarioadmin.html', {'form': form})

# Vista para la página agregar producto
@user_passes_test(lambda u: u.is_superuser)
def agregarproducto(request):
    form=CelularForm()
    if request.method == 'POST':
        
        form=CelularForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente.')
            return redirect(to="administracion")
            #Redirigir

    datos={
        "form":form
    }
    return render(request, 'mobilemart/agregarproducto.html', datos)

@user_passes_test(lambda u: u.is_superuser)
def eliminar_producto(request, id):
    celular = get_object_or_404(Celular, id=id)
    if request.method == 'POST':
        remove(path.join(str(settings.MEDIA_ROOT).replace('/media',''))+celular.foto.url)
        celular.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('administracion')
    
    datos={
        "celulares":celular
    }
    return render(request, 'mobilemart/eliminarproducto.html', datos)

# Vista para la página ventana edición (editar producto específico)
@user_passes_test(lambda u: u.is_superuser)
def ventanaedicion(request, id):
    celular = get_object_or_404(Celular, id=id)
    form = UpdateCelularForm(instance=celular)

    if request.method == "POST":
        form = UpdateCelularForm(data=request.POST, files=request.FILES, instance=celular)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto modificado correctamente.')
            return redirect('administracion')
        
    datos={
        "form":form,
        "celular":celular
    }
    return render(request, 'mobilemart/ventanaedicion.html', datos)

# Vista para la página crear usuario
@user_passes_test(lambda u: u.is_superuser)
def crearusuario(request): 
    form=CustomUserUpdateForm()
    if request.method == 'POST':
        
        form=CustomUserUpdateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente.')
            return redirect(to="listadousuarios")
            #Redirigir

    datos={
        "form":form
    }
    return render(request, 'mobilemart/crearusuario.html', datos)

@user_passes_test(lambda u: u.is_superuser)
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        try:
            usuario.delete()
            messages.success(request, 'Usuario eliminado correctamente.')
            return redirect('listadousuarios')
        except Exception as ex:
            messages.error(request, 'No se puede eliminar')
            return redirect('listadousuarios')
        
    datos={
        "usuario":usuario
    }
    return render(request, 'mobilemart/listadousuarios.html', datos)

# Vista para la página listado usuarios
@user_passes_test(lambda u: u.is_superuser)
def listadousuarios(request):
    usuarios=CustomUser.objects.all()
    
    datos={
        "usuarios":usuarios
    }
    return render(request, 'mobilemart/listadousuarios.html', datos)

# Vista para la página detalle-modificar usuario
@user_passes_test(lambda u: u.is_superuser)
def detalleusuario(request, pk):
    usuario = get_object_or_404(CustomUser, pk=pk)
    form = CustomUserUpdateForm(instance=usuario)

    if request.method == "POST":
        form = CustomUserUpdateForm(data=request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario modificado correctamente.')
            return redirect('listadousuarios')
        
    datos={
        "form":form,
        "usuario":usuario
    }
    
    return render(request, 'mobilemart/detalleusuario.html', datos)

@user_passes_test(lambda u: u.is_superuser)
def listadopedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'mobilemart/listadopedidos.html', {'pedidos': pedidos})

@user_passes_test(lambda u: u.is_superuser)
def detallepedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        form = ActualizarEstadoPedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('detallepedido', id=pedido.id)
    else:
        form = ActualizarEstadoPedidoForm(instance=pedido)
    return render(request, 'mobilemart/detallepedido.html', {'pedido': pedido, 'form': form})



