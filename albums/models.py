from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    date_released = models.DateField(null=True, blank=True)