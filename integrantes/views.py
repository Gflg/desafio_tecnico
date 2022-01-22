from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions
from integrantes.models import Integrantes
from integrantes.serializers import IntegranteSerializer


class IntegranteViewSet(viewsets.ModelViewSet):
    queryset = Integrantes.objects.all()
    serializer_class = IntegranteSerializer
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]
    permission_classes = (permissions.IsAdminUser,)

    def get_permissions(self):
        return [permissions.IsAdminUser()]