from servicos.models import Servicos
from rest_framework import serializers

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = ('id', 'name', 'description', 'service_type', 'is_available', 'created_at')