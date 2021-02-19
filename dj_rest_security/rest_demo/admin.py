from django.contrib import admin
from .models import Emp



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'salary', 'active']


admin.site.register(Emp, EmployeeAdmin)
