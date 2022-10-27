from django.db import models

class DomZona(models.Model):
    descripcionZona = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.descripcionZona)

class Domicilio(models.Model):
    domCalle = models.CharField(max_length=100)
    domNumero = models.BigIntegerField(blank=True)
    domBarrio = models.CharField(max_length=100)
    domLocalidad = models.CharField(max_length=100)
    domObservacion = models.CharField(max_length=200)
    domZona = models.ForeignKey(DomZona, on_delete=models.CASCADE)

    def __str__(self):
        impresion = "{0} - {1} - {2} - {3} - {4} - {5} - {6}"
        return impresion.format(self.domCalle, self.domNumero, self.domBarrio, self.domLocalidad, self.domObservacion,
                                self.domZona)

class Cliente(models.Model):
    cuil = models.CharField(max_length=11, unique=True)
    apellido = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=12, unique=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ('nombre',)

def __str__(self):
    impresion = "{0} - {1} - {2} - {3} - {4} - {5} - {6}"
    return impresion.format(self.cuil, self.apellido, self.nombre, self.fecha_nacimiento, self.telefono, self.domicilio)

