from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    producer = models.CharField(max_length=255)
    duration = models.IntegerField()  # Продолжительность в секундах

    def _str_(self):
        return self.title
# Create your models here.
