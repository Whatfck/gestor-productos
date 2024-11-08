from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()  # Cambiado de stock a cantidad
    disponibilidad = models.BooleanField(default=True)  # Nuevo campo para disponibilidad

    def __str__(self):
        return self.nombre