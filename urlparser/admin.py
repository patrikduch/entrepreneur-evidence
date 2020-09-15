from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    
    model = Task
	

# Register your models here.

admin.site.register(Task, TaskAdmin)
