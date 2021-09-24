from django.core.exceptions import RequestAborted
from django.db import models
from django.db.models.base import Model

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=32)
    hex_value = models.CharField(max_length=7, default="#001122")

    def __str__(self):
        return self.name

class CustomSettings(models.Model):
    name = models.CharField(max_length=32, default="color")
    value = models.ForeignKey(Color, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name