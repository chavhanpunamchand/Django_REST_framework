from django.db import models

# Create your models here.
#crud operations --> GET POST PUT PATCH OPTION DELETE-- HEAD
#APPLICATION -- POSTMAN
#CODING --> REQUESTS LIB

#SERIALIZE --> PYTHON OBJECT --JSON -->
            # 2 DIFF -->
            #CLIENT     SERI        DESER SERVER --> REQUEST
            #CLIENT     DESE        SER  SERVER -- RESPONSE
            
#Emp(id=101,name="PDC",age=30,salary=50000.0,active='Y')

class Emp(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.FloatField()
    active = models.CharField(max_length=10,default='Y')

    class Meta:
        db_table = 'EMP_INFO'