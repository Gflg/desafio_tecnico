from django.db import models
from uuid import uuid4

# Create your models here.

class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=50)
    theme = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)