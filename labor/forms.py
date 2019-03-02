from django import forms

from .models import (
    Employee,
    TaskClass,
    Task
)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = [
            'created_at',
            'updated_at',
            'completed',
            'duration',
            'labor_cost'
        ]
