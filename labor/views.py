from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    Employee,
    TaskClass,
    Task,
)

from .forms import (
    EmployeeForm,
    TaskForm,
)

def curr_time():
    return now()

def index(request):
    context = {
        'curr_time': curr_time(),
    }
    return render(request, 'labor/index.html', context)
