from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import (index, iphone, samsung, xiaomi, administracion, carrito, perfilusuario,
pedidosuser, iniciosesion, about, detalle_producto, recuperar_contrasena, registro_usuario, detalle_pedido_usuario,
agregarproducto, ventanaedicion, crearusuario, listadousuarios, detalleusuario, listadopedidos, detallepedido, eliminar_usuario)

urlpatterns = [
    path('',index,name='index'),
    path('iphone/', iphone, name='iphone'),
    path('samsung/', samsung, name='samsung'),
    path('xiaomi/', xiaomi, name='xiaomi'),
    path('administracion/', administracion, name='administracion'),
    path('carrito/', carrito, name='carrito'),
    path('perfilusuario/', perfilusuario, name='perfilusuario'),
    path('pedidosuser/', pedidosuser, name='pedidosuser'),
    path('iniciosesion/', iniciosesion, name='iniciosesion'),
    path('about/', about, name='about'),
    path('detalle_producto', detalle_producto, name='detalle_producto'),
    path('recuperarcontra/', recuperar_contrasena, name='recuperar_contrasena'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('detallepedidouser/', detalle_pedido_usuario, name='detalle_pedido_usuario'),
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    path('ventanaedicion/', ventanaedicion, name='ventanaedicion'),
    path('crearusuario/', crearusuario, name='crearusuario'),
    path('listadousuarios/', listadousuarios, name='listadousuarios'),
    path('detalleusuarios/<str:rut>/', detalleusuario, name='detalleusuario'),
    path('listadopedidos/', listadopedidos, name='listadopedidos'),
    path('detallepedido/', detallepedido, name='detallepedido'),
    path('eliminarusuario/<str:rut>/', eliminar_usuario, name='eliminarusuario'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)