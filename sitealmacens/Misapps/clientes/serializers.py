from dataclasses import field
from statistics import mode

from rest_framework import serializers
from Misapps.clientes.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__" #incluye todos los campos
        