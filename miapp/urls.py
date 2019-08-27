from django.urls import path
from .views import *

urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
    path('libros/', LibroList.as_view(), name = 'listar_libros'),
    path('libros/nuevo/', LibroCreate.as_view(), name = 'nuevo_libro'),
    path('libros/editar/<int:pk>', LibroUpdate.as_view(), name = 'actualizar_libro'),
    path('libros/eliminar/<int:pk>', LibroDelete.as_view(), name = 'eliminar_libro'),
    path('libros/detalle/<int:pk>', LibroDetalle.as_view(), name = 'detalle_libro'),
    path('ejemplar/',LibroEjemplares.as_view(), name='Ejemplares'),
    path('detalleEjemplar/<int:pk>',DetalleEjemplar.as_view(),name='Detalle_Ejemplar'),

]