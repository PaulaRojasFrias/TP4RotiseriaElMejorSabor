from django.db import models

class Empleado(models.Model):
    cuit = models.CharField(max_length=8, unique=True)
    nombre_completo = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    telefono_fijo = models.CharField(max_length=15)
    telefono_celular = models.CharField(max_length=15)
    calle= models.CharField(max_length=50)
    numero= models.PositiveIntegerField()
    localidad= models.CharField(max_length=50)
    departamento= models.CharField(max_length=50)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return '{}'.format(self.nombre_completo)

class Cadete(models.Model):
    cuit = models.CharField(max_length=8, unique=True)
    nombre_completo = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    telefono_fijo = models.CharField(max_length=15)
    telefono_celular = models.CharField(max_length=15)
    calle = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()
    localidad = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    vigencia_carnet = models.DateField()
    patente= models.CharField(max_length=10)
    codigo_zona = models.CharField(max_length=10)

    class Meta:
        ordering = ('nombre_completo',)

    def __str__(self):
        return '{}'.format(self.nombre_completo)
