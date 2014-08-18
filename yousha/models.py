from django.db import models

# Create your models here.
class HomeModel(models.Model):
    name = models.CharField(max_length=30)
