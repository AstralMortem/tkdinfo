from django.db import models
from django.conf import settings
import uuid

class APIToken(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    token = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.token) + f"-- {self.name}"