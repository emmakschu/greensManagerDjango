from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    GreensRolling,
    TeeRolling,
    FairwayRolling
)

from .forms import (
    GreensRollingForm,
    TeeRollingForm,
    FairwayRollingForm
)

def curr_time():
    return now()

def greensIndex(request):
    rollings = GreensRolling.objects.all().order_by('-roll_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'rollings': rollings,
    }
    
    return render(request, 'rolling/greens_index.html', context)
