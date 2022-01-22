from django.db import models
from uuid import uuid4


class Servicos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    service_type = models.IntegerField(null=False)
    is_available = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)