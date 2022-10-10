from django.db import models

# Create your models here.

class lohandsoft(models.Model):
    fullname = models.CharField(max_length=100)
    birth = models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    age= models.CharField(max_length=2)


class employee_list(models.Model):
    employee_id= models.CharField(max_length=10)
    employee_pass= models.CharField(max_length=10)