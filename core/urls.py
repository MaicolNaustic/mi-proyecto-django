from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('agregar_empresa/', views.agregar_empresa, name='agregar_empresa'),
    path('editar-empresa/<int:pk>/', views.editar_empresa, name='editar_empresa'),

    path('productos/', views.listar_productos, name='productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),

    path('trabajadores/', views.trabajadores, name='trabajadores'),
    path('trabajadores/agregar/', views.agregar_trabajador, name='agregar_trabajador'),
    path('trabajadores/<int:pk>/editar/', views.editar_trabajador, name='editar_trabajador'),
    path('trabajadores/<int:pk>/eliminar/', views.eliminar_trabajador, name='eliminar_trabajador'),

    path('proveedores/', views.listar_proveedores, name='proveedores'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:proveedor_id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
]
