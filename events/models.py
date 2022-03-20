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

    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    profile = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE, related_name="reviews", null=True)
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="reviews", null=True)
    
    rating = models.IntegerField(choices=Rating.choices)
    text = models.TextField()

def __str__(self):
        return self.text


    
