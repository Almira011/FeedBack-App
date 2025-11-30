from django.db import models

# Create your models here.

class Reviewtable(models.Model):
    username = models.CharField(max_length=100)
    review_text = models.CharField(max_length=1000)
    rating = models.IntegerField()