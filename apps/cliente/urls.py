from django.urls import path
from .views import cliente

urlpatterns = [
    path('', cliente, name='admin-cliente'),
]