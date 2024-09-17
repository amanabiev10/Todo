from django.contrib import admin
from .models import Task

admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass