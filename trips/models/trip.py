from django.db import models

class Trip(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField("trip date")
    duration = models.DurationField(max_length=45)
    location = models.CharField(max_length=255)
    # user_id = models.ForeignKey(on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name