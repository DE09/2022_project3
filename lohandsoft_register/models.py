from django.db import models

# Create your models here.

class lohandsoft(models.Model):
    fullname = models.CharField(max_length=100)
    birth = models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    age= models.CharField(max_length=2)