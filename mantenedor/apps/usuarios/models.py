from django.db import models

# Create your models here.
class Usuario(models.Model):
    email = models.CharField(max_length=50)
    run = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=200)
    fecha_nacimiento = models.DateTimeField()
    telefono_contacto = models.CharField(max_length=9)
    usuario = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre_completo