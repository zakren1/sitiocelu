from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import (index, iphone, samsung, xiaomi, administracion, ver_carrito, agregar_al_carrito, actualizar_carrito, 
eliminar_item_carrito, confirmar_carrito, perfilusuario, perfilusuarioadmin, pedidosuser, about, detalle_producto, recuperar_contrasena,
RegistroView, detalle_pedido_usuario, agregarproducto, ventanaedicion, crearusuario, listadousuarios, detalleusuario, listadopedidos, 
detallepedido, eliminar_usuario, eliminar_producto, CustomLoginView, cerrar_sesion, redirect_login,)

urlpatterns = [
    path('',index,name='index'),
    path('iphone/', iphone, name='iphone'),
    path('samsung/', samsung, name='samsung'),
    path('xiaomi/', xiaomi, name='xiaomi'),
    path('administracion/', administracion, name='administracion'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('agregarcarrito/<int:id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/actualizar/<int:id>/', actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/<int:id>/', eliminar_item_carrito, name='eliminar_item_carrito'),
    path('confirmar_carrito', confirmar_carrito, name='confirmar_carrito'),
    path('perfilusuario/', perfilusuario, name='perfilusuario'),
    path('perfilusuarioadmin/', perfilusuarioadmin, name='perfilusuarioadmin'),
    path('pedidosuser/', pedidosuser, name='pedidosuser'),
    path('about/', about, name='about'),
    path('detalleproducto/<int:id>/', detalle_producto, name='detalle_producto'),
    path('recuperarcontra/', recuperar_contrasena, name='recuperar_contrasena'),
    path('registro/', RegistroView.as_view(), name='registro_usuario'),
    path('detallepedidouser/<int:id>/', detalle_pedido_usuario, name='detalle_pedido_usuario'),
    path('agregarproducto/', agregarproducto, name='agregarproducto'),
    path('ventanaedicion/<int:id>/', ventanaedicion, name='ventanaedicion'),
    path('crearusuario/', crearusuario, name='crearusuario'),
    path('listadousuarios/', listadousuarios, name='listadousuarios'),
    path('detalleusuario/<int:pk>/', detalleusuario, name='detalleusuario'),
    path('listadopedidos/', listadopedidos, name='listadopedidos'),
    path('detallepedido/<int:id>/', detallepedido, name='detallepedido'),
    path('eliminarusuario/<int:pk>/', eliminar_usuario, name='eliminarusuario'),
    path('eliminarproducto/<int:id>/', eliminar_producto, name='eliminarproducto'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('cerrar_sesion',cerrar_sesion, name='cerrar_sesion'),
    path('redirect/', redirect_login, name='redirect_login'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)