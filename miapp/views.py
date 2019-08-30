from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Libro,Ejemplar,Prestamo
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
def cargar_inicio(request):
    return render(request,"miapp/index.html")

#libro
class LibroList(ListView):
    model = Libro 
    template_name = 'miapp/lista_libros.html'

class LibroCreate(LoginRequiredMixin, CreateView):
    model = Libro
    fields = ["nombre","descripcion","isbn"]
    template_name = 'miapp/nuevo_libro.html'
    success_url = reverse_lazy('Listar_libros')

class LibroUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    fields = ["nombre","descripcion","isbn"]
    template_name = 'miapp/actualizar_libro.html'
    success_url = reverse_lazy('Listar_libros')
class LibroDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = 'miapp/eliminar_libro.html'
    success_url = reverse_lazy('Listar_libros')
class LibroDetalle(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = 'miapp/detalle_libro.html'
#ejemplar
class EjemplarList(ListView):
    model = Ejemplar
    template_name = 'miapp/ejemplarlist.html'

class DetalleEjemplar(DetailView):
    model = Ejemplar
    template_name = 'miapp/detalle_ejemplar.html'

class EjemplarUpdate(LoginRequiredMixin, UpdateView):
    model = Ejemplar
    fields = ["numeroejemplar","Libro","fechadecompra"]
    template_name = 'miapp/actualizar_ejemplar.html'
    success_url = reverse_lazy('Ejemplar')
    
class EjemplarDelete(LoginRequiredMixin, DeleteView):
    model = Ejemplar
    template_name = 'miapp/eliminar_ejemplar.html'
    success_url = reverse_lazy('Ejemplar')
    
class EjemplarCreate(LoginRequiredMixin, CreateView):
    model = Ejemplar
    fields = ["numeroejemplar","Libro","fechadecompra"]
    template_name = 'miapp/nuevo_ejemplar.html'
    success_url = reverse_lazy('Ejemplar')
#prestamo
class PrestamoList(ListView):
    model=Prestamo
    template_name = 'miapp/prestamo.html'

class PrestamoCreate(LoginRequiredMixin, CreateView):
    model=Prestamo
    fields = ["fechaprestamo", "nombre_cliente", "telefono", "estado"]
    template_name = 'miapp/nuevo_prestamo.html'
    success_url = reverse_lazy('prestamo')

class PrestamoUpdate(LoginRequiredMixin, UpdateView):
    model=Prestamo
    fields = ["fechaprestamo", "nombre_cliente", "telefono", "estado"]
    template_name = 'miapp/editar_prestamo.html'
    success_url = reverse_lazy('prestamo')

class PrestamoDelete(LoginRequiredMixin, DeleteView):
    model=Prestamo
    template_name = 'miapp/eliminar_prestamo.html'
    success_url = reverse_lazy('prestamo')