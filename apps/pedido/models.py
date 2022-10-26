from django.db import models
from apps.cliente.models import Cliente
from apps.empleado.models import Cadete
# Create your models here.
class TipoPlato(models.Model):
    descripcion= models.CharField(max_length=50)

class TipoMenu(models.Model):
    descripcion = models.CharField(max_length=50)

class Estado(models.Model):
    descripcion = models.CharField(max_length=50)

class TipoEntrega(models.Model):
    descripcion = models.CharField(max_length=50)

class Plato(models.Model):
    nombre_plato = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    tipo_plato = models.ForeignKey(TipoPlato, on_delete=models.CASCADE)
    tipo_menu = models.ForeignKey(TipoMenu, on_delete=models.CASCADE)
    precio = models.CharField(max_length=4)
    vigente = models.BooleanField()

class Pedido(models.Model):
    fecha_pedido = models.DateField()
    estado_pedido = models.ForeignKey(Estado, on_delete=models.CASCADE)
    tipo_entrega = models.ForeignKey(TipoEntrega, on_delete=models.CASCADE)
    horaInicioEntrega = models.TimeField()
    horaFinEntrega = models.TimeField()
    plato = models.ManyToManyField(Plato)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cadete = models.ForeignKey(Cadete, on_delete=models.CASCADE)
