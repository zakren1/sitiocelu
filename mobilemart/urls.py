from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import (index, iphone, samsung, xiaomi, administracion, carrito, perfilusuario, pedidosuser, about,
detalle_producto, recuperar_contrasena, registro_usuario, detalle_pedido_usuario, agregarproducto, ventanaedicion, 
crearusuario, listadousuarios, detalleusuario, listadopedidos, detallepedido, eliminar_usuario, eliminar_producto, cerrar_sesion)

urlpatterns = [
    path('',index,name='index'),
    path('iphone/', iphone, name='iphone'),
    path('samsung/', samsung, name='samsung'),
    path('xiaomi/', xiaomi, name='xiaomi'),
    path('administracion/', administracion, name='administracion'),
    path('carrito/', carrito, name='carrito'),
    path('perfilusuario/', perfilusuario, name='perfilusuario'),
    path('pedidosuser/', pedidosuser, name='pedidosuser'),
    path('about/', about, name='about'),
    path('detalleproducto/<int:id>/', detalle_producto, name='detalle_producto'),
    path('recuperarcontra/', recuperar_contrasena, name='recuperar_contrasena'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('detallepedidouser/', detalle_pedido_usuario, name='detalle_pedido_usuario'),
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    path('ventanaedicion/<int:id>/', ventanaedicion, name='ventanaedicion'),
    path('crearusuario/', crearusuario, name='crearusuario'),
    path('listadousuarios/', listadousuarios, name='listadousuarios'),
    path('detalleusuario/<str:rut>/', detalleusuario, name='detalleusuario'),
    path('listadopedidos/', listadopedidos, name='listadopedidos'),
    path('detallepedido/', detallepedido, name='detallepedido'),
    path('eliminarusuario/<str:rut>/', eliminar_usuario, name='eliminarusuario'),
    path('eliminarproducto/<int:id>/', eliminar_producto, name='eliminarproducto'),
    path('cerrar_sesion',cerrar_sesion, name='cerrar_sesion')
    #path('iniciosesion/', iniciosesion, name='iniciosesion'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)