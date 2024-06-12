from django.db import models
from django.utils import timezone

class ButtonPress(models.Model):
    username = models.CharField(max_length=255)
    url = models.URLField()
    timestamp = models.DateTimeField(default=timezone.now)

class Neon(models.Model):  # New Neon model
    timestamp = models.DateTimeField(auto_now_add=True)