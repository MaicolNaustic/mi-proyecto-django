from django.db import models  # ← esta línea es imprescindible

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()  # este campo es nuevo
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre
