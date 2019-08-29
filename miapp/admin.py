from django.contrib import admin

from .models import *


admin.site.register(Libro)
#admin.site.register(Prestamo)
admin.site.register(DetallePrestamo)
admin.site.register(Ejemplar)

class DetallePrestamoinline(admin.TabularInline):
    model=DetallePrestamo

class PrestamoAdmin(admin.ModelAdmin):
    inlines = [
        DetallePrestamoinline,
    ]
admin.site.register(Prestamo,PrestamoAdmin)