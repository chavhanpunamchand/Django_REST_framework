from django.db import models

# Create your models here.


class Emp(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    role = models.CharField(max_length=40)

    class Meta:
        db_table = 'EMP_INFO'