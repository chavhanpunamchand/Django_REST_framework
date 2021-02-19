from django.db import models


# Employee(eno=101,ename="Punamchand",esal=55000.00,eaddr="Pune")
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=64)

    class Meta:
        db_table = 'Employee_Info'
