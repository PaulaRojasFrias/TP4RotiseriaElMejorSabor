from django.db import models

from TP4RotiseriaElMejorSabor.apps.cliente.models import Cliente
from TP4RotiseriaElMejorSabor.apps.empleado.models import Cadete


# Create your models here.

class Plato(models.Model):
    TIPO_PLATO_OPCIONES = (
        ('entrada', 'Entrada'),
        ('plato principal', 'Plato principal'),
        ('postre', 'Postre'),
    )

    TIPO_MENU_OPCIONES = (
        ('vegetariano', 'Vegetariano'),
        ('celiaco', 'Celiaco'),
        ('diabetico', 'Diabetico'),
        ('normal', 'Normal'),
    )

    codigo_plato = models.CharField(max_length=11, unique=True)
    nombre_plato = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    tipo_plato = models.CharField(max_length=20, choices=TIPO_PLATO_OPCIONES)
    precio = models.CharField(max_length=4)
    vigente = models.BooleanField()
    tipo_menu = models.CharField(max_length=20, choices=TIPO_MENU_OPCIONES)


class Pedido(models.Model):
    ESTADO_OPCIONES = (
        ('pendiente', 'Pendiente'),
        ('en camino', 'En camino'),
        ('cancelado', 'Cancelado'),
        ('entregado', 'Entregado'),
        ('devuelto', 'Devuelto'),

    )

    ENTREGA_OPCIONES = (
        ('domicilio', 'Domicilio'),
        ('local', 'Local'),
    )
    codigoPedido = models.CharField(max_length=11, unique=True)
    fecha_pedido = models.DateField()
    estado_pedido = models.CharField(max_length=15, choices= ESTADO_OPCIONES)
    tipo_entrega = models.CharField(max_length=9, choices= ENTREGA_OPCIONES)
    horaInicioEntrega = models.TimeField()
    horaFinEntrega = models.TimeField()
    plato = models.ManyToManyField(Plato)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cadete = models.ForeignKey(Cadete, on_delete=models.CASCADE)
