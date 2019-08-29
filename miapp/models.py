from django.db import models

class Libro(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=500)
    isbn = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre

class Ejemplar(models.Model):
    numeroejemplar = models.CharField(max_length=45)
    fechadecompra = models.DateField(null=False)
    Libro = models.ForeignKey('Libro',on_delete=models.CASCADE) 
    def __str__(self):
        return self.numeroejemplar +"-> " +str(self.Libro) 

class Prestamo(models.Model):
    fechaprestamo = models.DateField("Fecha de prestamo")
    nombre_cliente = models.CharField(max_length=40)
    telefono = models.CharField(max_length=45)
    estado = models.BooleanField()
    def __str__(self):
        return "{0}-{1}".format(self.fechaprestamo, self.nombre_cliente)

class DetallePrestamo(models.Model):
    fechaDeDevolucion = models.DateField("fecha de devolucion", null=True)
    Prestamo = models.ForeignKey('Prestamo',on_delete=models.CASCADE)
    Ejemplar = models.ForeignKey('Ejemplar',on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0}-{1}" .format(self.Prestamo, self.Ejemplar)