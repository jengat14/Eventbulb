from datetime import datetime
from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)

def __str__(self):
        return self.title
