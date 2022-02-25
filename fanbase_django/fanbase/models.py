
from django.db import models

# Create models here.


class Memory(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    photo_url = models.TextField()
    social_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
