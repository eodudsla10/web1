from django.db import models

# Create your models here.

class shop(models.Model):
    objects = models.Manager()
    title =models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    subject =models.CharField(max_length=255)
    field =models.TextField()
