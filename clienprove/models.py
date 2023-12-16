from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    Nombre = models.CharField(max_length=64, default='nombre')
    Apellido = models.CharField(max_length=64, default='Apellido')
    telefono = models.CharField(max_length=20, default='Telefono')  
    email = models.EmailField()
    descripcion = models.CharField(max_length=100)

class Proveedor(models.Model):
    Nombre = models.CharField(max_length=64, default='nombre')
    Apellido = models.CharField(max_length=64, default='Apellido')
    telefono = models.CharField(max_length=20, default='Telefono')
    email = models.EmailField()
    descripcion = models.CharField(max_length=100)


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    producto = models.CharField(max_length=100, default='Producto')
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        # Calculate total before saving
        self.total = self.cantidad * self.precio
        super().save(*args, **kwargs)

