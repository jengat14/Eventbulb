from datetime import datetime
from django.db import models
# from accounts.models import UserProfile


# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)

def __str__(self):
        return self.title

class Review(models.Model):
    profile = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField
    review_text = models.TextField()

def __str__(self):
        return self.text


    
