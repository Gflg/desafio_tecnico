from integrantes.models import Integrantes
from rest_framework import serializers


class IntegranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrantes
        fields = ('id', 'name', 'birth_date', 'address', 'service_area', 'is_allocated', 'joined_at')