from django.contrib import admin

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
