from django.urls import path
from miapp.views import *

urlpatterns = [
    path('',cargar_inicio, name='Inicio'),
    path('libro/',LibroList.as_view(), name='Listar_libros'),
    path('libro/nuevo/',LibroCreate.as_view(),name='Nuevo_libro'),
    path('libro/editar/<int:pk>',LibroUpdate.as_view(),name='Editar_Libro'),
    path('libro/eliminar/<int:pk>',LibroDelete.as_view(),name='Borrar_Libro'),
    path('libro/detalle/<int:pk>',LibroDetalle.as_view(),name='Detalle_Libro'),
    path('ejemplar/',EjemplarList.as_view(),name='Ejemplar'),
    path('detalle_ejemplar/<int:pk>',DetalleEjemplar.as_view(),name='Detalle_Ejemplar'),
    path('ejemplar/editar/<int:pk>',EjemplarUpdate.as_view(),name='Editar_Ejemplar'),
    path('ejemplar/eliminar/<int:pk>',EjemplarDelete.as_view(),name='Eliminar_Ejemplar'),
    path('ejemplar/nuevo/',EjemplarCreate.as_view(),name='Nuevo_Ejemplar'),
]