# clienprove/urls.py
from django.urls import path
from .views import  index, add_cliente, add_proveedor, show_clientes, show_proveedores, detalle_cliente, detalle_proveedor
from .views import crear_factura, mostrar_facturas, editar_factura, eliminar_factura, factura_editada, ver_factura

urlpatterns = [
    path('', index, name='base'),
    path('add_cliente/', add_cliente, name='add_cliente'),
    path('add_proveedor/', add_proveedor, name='add_proveedor'),
    path('show_clientes', show_clientes, name='show_clientes' ),
    path('show_proveedores', show_proveedores, name='show_proveedores' ),
    path('cliente_info/<int:cliente_id>/', detalle_cliente, name='cliente_info'),
    path('proveedor_info/<int:proveedor_id>/', detalle_proveedor, name='proveedor_info'),
    path('crear_factura/<int:cliente_id>/', crear_factura, name='crear_factura'),
    path('mostrar_facturas/<int:cliente_id>/', mostrar_facturas, name='mostrar_facturas'),
    path('editar_factura/<int:factura_id>/', editar_factura, name='editar_factura'),
    path('eliminar_factura/<int:factura_id>/', eliminar_factura, name='eliminar_factura'),
    path('factura_editada/<int:factura_id>/', factura_editada, name='factura_editada'),
     path('ver_factura/<int:factura_id>/', ver_factura, name='ver_factura'),
]


    
