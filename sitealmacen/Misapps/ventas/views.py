from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import generics

from rest_framework import status

from Misapps.ventas.models import Venta
from Misapps.ventas.serializers import VentaSerializer

# Create your views here.


class VentaList(generics.ListCreateAPIView):
    """
    Lista de Ventas
    """

    queryset = Venta.objects.all()
    serializer_class = VentaSerializer



class VentaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete de los clientes por pk
    """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
