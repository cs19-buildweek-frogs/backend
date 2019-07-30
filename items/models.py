from django.db import models

# Create your models here.
class Items(models.Model):
    title = models.TextField()
    description = models.TextField()
