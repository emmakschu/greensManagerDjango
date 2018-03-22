from django.shortcuts import render
from django.utils.timezone import now

from fertilizing.models import (
    Fertilizer,
    Fertilizing,
    GreensFert,
    TeeFert,
    FairwayFert,
    RoughFert
)


curr_time = now()

def index(request):

    all_fert = Fertilizing.objects.all().order_by('-fert_date')[:5]
    
    context = {
        'curr_time': curr_time,
        'all_fert': all_fert,
    }
    return render(request, 'fertilizing/index.html', context)

def newFert(request):
    return render(request, 'fertilizing/newFert.html')
