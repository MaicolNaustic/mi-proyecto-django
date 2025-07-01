from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    ruc = models.CharField(max_length=13)
    direccion = models.CharField(max_length=255)
    anio_fundacion = models.IntegerField()
    mision = models.TextField()
    vision = models.TextField()
    imagen = models.ImageField(upload_to='empresa/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    codigo_empleado = models.CharField(max_length=50)
    otros_datos = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='trabajadores/', blank=True, null=True)

    def __str__(self):
        return self.nombre
