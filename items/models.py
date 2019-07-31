from django.db import models

# Create your models here.
class Items(models.Model):
    title       = models.CharField(max_length=120) #max_legnth = required
    description = models.TextField()
