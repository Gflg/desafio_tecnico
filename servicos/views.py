from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions
from servicos.models import Servicos
from servicos.serializers import ServicoSerializer

# Create your views here.

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = ServicoSerializer
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]
    permission_classes = (permissions.IsAdminUser,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]