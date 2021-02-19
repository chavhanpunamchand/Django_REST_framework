from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField
    email = models.EmailField(max_length=30,default='NA')

    class Meta:
        db_table = 'EMP_INFO'
