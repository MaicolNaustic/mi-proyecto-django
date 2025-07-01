from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    ruc = models.CharField(max_length=13)
    direccion = models.CharField(max_length=255)
    mision = models.TextField()
    vision = models.TextField()
    imagen = models.ImageField(upload_to='empresa/', blank=True, null=True)
    anio_fundacion = models.PositiveIntegerField()  # ← sin tilde

    def __str__(self):
        return self.nombre
