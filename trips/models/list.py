from django.db import models
from .trip import Trip

class List(models.Model):
    trip = models.ForeignKey(Trip, related_name="lists", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name