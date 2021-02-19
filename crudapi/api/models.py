from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=40)

    class Meta:
        db_table = 'student_info'
