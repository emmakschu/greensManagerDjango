from django.contrib import admin

from .models import (
    Employee,
    TaskClass,
    Task
)

admin.site.register(Employee)
admin.site.register(Task)
