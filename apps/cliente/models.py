from django.db import models

# Create your models here.

class Cliente(models.Model):
   OPCIONES_ZONA = (
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste'),
    )

cuil = models.CharField(max_length=11, unique=True)
nombre = models.CharField(max_length=200)
domCalle = models.CharField(max_length=100)
domNumero = models.CharField(max_length=4, unique=True)
domBarrio = models.CharField(max_length=100)
domLocalidad = models.CharField(max_length=100)
domObservacion = models.CharField(max_length=200)

telefono = models.CharField(max_length=12, unique=True)

creado = models.DateTimeField(auto_now_add=True)
modificado = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ('nombre',)

def __str__(self):
    return '{}'.format(self.nombre)
