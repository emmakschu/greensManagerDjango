from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    Aerating,
    GreensAerating,
    TeeAerating,
    FairwayAerating,
    RoughAerating
)

from .forms import (
    AeratingForm,
    GreensAeratingForm,
    TeeAeratingForm,
    FairwayAeratingForm,
    RoughAeratingForm,
)

def curr_time():
    return now()

def index(request):
    aeratings = Aerating.objects.all().order_by('-aerate_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'aeratings': aeratings,
    }
    
    return render(request, 'aerating/index.html', context)

def greensIndex(request):
    aeratings = GreensAerating.objects.all().order_by(
        '-aerate_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'aeratings': aeratings,
    }
    
    return render(request, 'aerating/greens_index.html', context)
    
def greensNew(request):
    form = GreensAeratingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'aerating/greens_new.html', context)

def greensCreate(request):
    if request.method == 'POST':
        form = GreensAeratingForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('aerate:greens_detail', pk=pending_form.pk)

def greensDetail(request, pk):
    aerating = GreensAerating.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'aerating': aerating,
    }
    
    return render(request, 'aerating/greens_detail.html', context)

def greensEdit(request, pk):
    aerating = GreensAerating.objects.get(pk=pk)
    form = GreensAeratingForm(instance=aerating)
    
    context = {
        'curr_time': curr_time(),
        'aerating': aerating,
        'form': form,
    }
    
    return render(request, 'aerating/greens_edit.html', context)

def greensUpdate(request, pk):
    aerating = GreensAerating.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = GreensAeratingForm(request.POST, instance=aerating)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('aerate:greens_detail', pk=aerating.pk)
