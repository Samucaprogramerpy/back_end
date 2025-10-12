from django.db import models

# Create your models here.
class User(models.Model) : 
    nome = models.CharField(max_length=20, default='')
    senha = models.CharField(max_length=128, null=False, blank=False, default='')
