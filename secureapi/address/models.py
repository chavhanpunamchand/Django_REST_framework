from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=40)
    pincode = models.IntegerField()
    state = models.CharField(max_length=40)

    class Meta:
        db_table = 'ADR_INFO'


class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'STUDENT_INFO'


class Courses(models.Model):
    coursename = models.CharField(max_length=40)
    coursefees = models.IntegerField()
    students = models.ForeignKey(Student,on_delete=models.CASCADE,
                                 related_name='courses')
    class Meta:
        db_table = 'COURSE_INFO'