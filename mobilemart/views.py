from django.shortcuts import render
from .models import Usuario, Celular

# Create your views here.
def index(request):
    return render(request,'mobilemart/index.html')


# Vista para la página de Apple
def iphone(request):
    return render(request, 'mobilemart/iphone.html')

# Vista para la página de Samsung
def samsung(request):
    return render(request, 'mobilemart/samsung.html')

# Vista para la página de Xiaomi
def xiaomi(request):
    return render(request, 'mobilemart/xiaomi.html')

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
def iniciosesion(request):
    return render(request, 'mobilemart/InicioSesion.html')

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
    return render(request, 'mobilemart/RegistroUser.html')

# Vista para la página detalle pedido usuario
def detalle_pedido_usuario(request):
    return render(request, 'mobilemart/detallepedidouser.html')

##### VISTAS DE ADMINISTRADOR #####

# Vista para la página de Administración (editarproducto)
def administracion(request):
    return render(request, 'mobilemart/editarproducto.html')

# Vista para la página agregar producto
def agregarproducto(request):
    return render(request, 'mobilemart/agregarproducto.html')

# Vista para la página ventana edición (editar producto específico)
def ventanaedicion(request):
    return render(request, 'mobilemart/ventanaedicion.html')

# Vista para la página crear usuario
def crearusuario(request):
    return render(request, 'mobilemart/crearusuario.html')

# Vista para la página listado usuarios
def listadousuarios(request):
    return render(request, 'mobilemart/listadousuarios.html')

# Vista para la página detalle usuario
def detalleusuario(request):
    return render(request, 'mobilemart/detalleusuario.html')

# Vista para la página listado pedidos
def listadopedidos(request):
    return render(request, 'mobilemart/listadopedidos.html')

# Vista para la página detalle pedido
def detallepedido(request):
    return render(request, 'mobilemart/detallepedido.html')



