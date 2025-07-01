from django.db import models

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    codigo_empleado = models.CharField(max_length=50)
    otros_datos = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='trabajadores/', blank=True, null=True)

    def __str__(self):
        return self.nombre
