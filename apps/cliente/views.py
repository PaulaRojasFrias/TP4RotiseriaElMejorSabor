from django.shortcuts import render
from django.http import HttpResponse

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Cliente

def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request,
                  'cliente/clientes.html',
                  {'clientes': clientes})

def cliente_detalle(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request,
                  'cliente/clientes.html',
                  {'cliente': cliente})