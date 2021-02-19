from django.contrib import admin
from .models import Employee


# Employee(eno=101,ename="Punamchand",esal=55000.00,eaddr="Pune")
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']

