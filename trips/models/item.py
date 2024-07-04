from django.db import models
from .list import List

class Item(models.Model):
    list = models.ForeignKey(List, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.FloatField(max_length=45)
    unit = models.CharField(max_length=45)
    is_packed = models.BooleanField(default=0)
    # notes = models.CharField(max_length=255) **FUTURE**

    def __str__(self) -> str:
        return self.name