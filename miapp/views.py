from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Libro,Ejemplar

def cargar_inicio(request):
    return render(request,"miapp/index.html")

class LibroList(ListView):
    model = Libro 
    template_name = 'miapp/lista_libros.html'

class LibroCreate(CreateView):
    model = Libro
    fields = ["nombre","descripcion","isbn"]
    template_name = 'miapp/nuevo_libro.html'
    success_url = reverse_lazy('Listar_libros')

class LibroUpdate(UpdateView):
    model = Libro
    fields = ["nombre","descripcion","isbn"]
    template_name = 'miapp/actualizar_libro.html'
    success_url = reverse_lazy('Listar_libros')
class LibroDelete(DeleteView):
    model = Libro
    template_name = 'miapp/eliminar_libro.html'
    success_url = reverse_lazy('Listar_libros')
class LibroDetalle(DetailView):
    model = Libro
    template_name = 'miapp/detalle_libro.html'

class EjemplarList(ListView):
    model = Ejemplar
    template_name = 'miapp/ejemplarlist.html'

class DetalleEjemplar(DetailView):
    model = Ejemplar
    template_name = 'miapp/detalle_ejemplar.html'

class EjemplarUpdate(UpdateView):
    model = Ejemplar
    fields = ["numeroejemplar","Libro","fechadecompra"]
    template_name = 'miapp/actualizar_ejemplar.html'
    success_url = reverse_lazy('Ejemplar')
    
class EjemplarDelete(DeleteView):
    model = Ejemplar
    template_name = 'miapp/eliminar_ejemplar.html'
    success_url = reverse_lazy('Ejemplar')
    
class EjemplarCreate(CreateView):
    model = Ejemplar
    fields = ["numeroejemplar","Libro","fechadecompra"]
    template_name = 'miapp/nuevo_ejemplar.html'
    success_url = reverse_lazy('Ejemplar')