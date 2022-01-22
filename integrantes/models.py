from django.db import models
from uuid import uuid4
from servicos.models import Servicos

DEFAULT_SERVICE_AREA_ID = 1


class Integrantes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=False)
    address = models.CharField(max_length=500)
    service_area = models.ForeignKey(Servicos, on_delete=models.CASCADE, null=False, default=DEFAULT_SERVICE_AREA_ID)
    is_allocated = models.BooleanField(null=False, default=False)
    joined_at = models.DateTimeField(auto_now_add=True)