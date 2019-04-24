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

def greensNew(request):
    form = GreensRollingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'rolling/greens_new.html', context)

def greensCreate(request):
    if request.method == 'POST':
        form = GreensRollingForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('roll:greens_detail', pk=pending_form.pk)

def greensDetail(request, pk):
    rolling = GreensRolling.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'rolling': rolling,
    }
    
    return render(request, 'rolling/greens_detail.html', context)

def greensEdit(request, pk):
    rolling = GreensRolling.objects.get(pk=pk)
    form = GreensRollingForm(instance=rolling)
    
    context = {
        'curr_time': curr_time(),
        'rolling': rolling,
        'form': form,
    }
    
    return render(request, 'rolling/greens_edit.html', context)

def greensUpdate(request, pk):
    rolling = GreensRolling.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = GreensRollingForm(request.POST, instance=rolling)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('roll:greens_detail', pk=rolling.pk)

def teesIndex(request):
    rollings = TeeRolling.objects.all().order_by('-roll_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'rollings': rollings,
    }
    
    return render(request, 'rolling/tees_index.html', context)

def teesNew(request):
    form = TeeRollingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'rolling/tees_new.html', context)

def teesCreate(request):
    if request.method == 'POST':
        form = TeeRollingForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('roll:tees_detail', pk=pending_form.pk)

def teesDetail(request, pk):
    rolling = TeeRolling.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'rolling': rolling,
    }
    
    return render(request, 'rolling/tees_detail.html', context)

def teesEdit(request, pk):
    rolling = TeeRolling.objects.get(pk=pk)
    form = TeeRollingForm(instance=rolling)
    
    context = {
        'curr_time': curr_time(),
        'rolling': rolling,
        'form': form,
    }
    
    return render(request, 'rolling/tees_edit.html', context)

def teesUpdate(request, pk):
    rolling = TeeRolling.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = TeeRollingForm(request.POST, instance=rolling)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('roll:tees_detail', pk=rolling.pk)
