from django.db import models
from uuid import uuid4
from integrantes.models import Integrantes

DEFAULT_AUTHOR_ID = 1


class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(Integrantes, on_delete=models.CASCADE, null=False, default=DEFAULT_AUTHOR_ID)
    theme = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)