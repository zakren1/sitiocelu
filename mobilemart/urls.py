
from django.urls import include, path

from .views import index, iphone, samsung, xiaomi, administracion, carrito, perfilusuario, pedidosuser,InicioSesion,about,detalle_producto,recuperar_contrasena,registro_usuario,detalle_pedido_usuario

urlpatterns = [
    path('',index,name='index'),
    path('iphone/', iphone, name='iphone'),
    path('samsung/', samsung, name='samsung'),
    path('xiaomi/', xiaomi, name='xiaomi'),
    path('administracion/', administracion, name='administracion'),
    path('carrito/', carrito, name='carrito'),
    path('perfilusuario/', perfilusuario, name='perfilusuario'),
    path('pedidosuser/', pedidosuser, name='pedidosuser'),
    path('InicioSesion/', InicioSesion, name='InicioSesion'),
    path('about/', about, name='about'),
    path('detalle_producto', detalle_producto, name='detalle_producto'),
    path('recuperarcontra/', recuperar_contrasena, name='recuperar_contrasena'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('detallepedidouser/', detalle_pedido_usuario, name='detalle_pedido_usuario'),
]
