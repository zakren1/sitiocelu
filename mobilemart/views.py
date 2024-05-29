from django.shortcuts import render

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

# Vista para la página de Administración
def administracion(request):
    return render(request, 'mobilemart/administracion.html')

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
def InicioSesion(request):
    return render(request, 'mobilemart/InicioSesion.html')

# Vista para la página Acerca de
def about(request):
    return render(request, 'mobilemart/about.html')

# Vista para la página detalle producto
def detalle_producto(request):
    return render(request, 'mobilemart/iphone15pro.html')

# Vista para la página recuperar contraseña
def recuperar_contrasena(request):
    return render(request, 'mobilemart/recuperarcontra.html')

# Vista para la página registro usuario
def registro_usuario(request):
    return render(request, 'mobilemart/RegistroUser.html')

# Vista para la página detalle pedido usuario
def detalle_pedido_usuario(request):
    return render(request, 'mobilemart/detallepedidouser.html')