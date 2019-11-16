from django.db import models
from django.utils import timezone


class Producto(models.Model):
    id_producto = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    estado = models.BooleanField(default = False)
    stock = models.IntegerField()
    equipo = models.CharField(max_length=30, blank = True)
    imagen_front = models.ImageField(upload_to = 'imagen/productos',null = True, blank = True)
    imagen_back = models.ImageField(upload_to = 'imagen/productos', null = True, blank = True)
    
    def __str__(self):
        return self.nombre
