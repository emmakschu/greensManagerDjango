from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (

)


def index(request):
    return render(request, 'labor/index.html')

def mowIndex(request):
    mowing = Mow
