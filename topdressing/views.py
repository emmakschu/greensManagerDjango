from django.shortcuts import render, redirect
from django.conf.timezone import now

from .models import (
    SandType,
    Topdressing,
    GreenTopdressing,
    TeeTopdressing,
    FairwayTopdressing
)

def curr_time():
    return now()

def index(request):
    context = {
        'curr_time': curr_time(),
    }
    
    return render(request, 'topdressing/index.html', context)

def sandIndex(request):
    sands = SandType.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'sands': sands,
    }
    
    return render(request, 'topdressing/sand_index.html', context)

def sandNew(request):
    form = SandTypeForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'topdressing/sand_new.html', context)

def sandCreate(request):
    if request.method == 'POST':
        form = SandTypeForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            pending_form.save()
        
    return redirect('topd:sand_detail', pk=pending_form.pk)

def sandDetail(request, pk):
    sand = SandType.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'sand': sand,
    }
    
    return render(request, 'topdressing/sand_detail.html', context)

def sandEdit(request, pk):
    sand = SandType.objects.get(pk=pk)
    form = SandTypeForm(instance=sand)
    
    context = {
        'curr_time': curr_time(),
        'sand': sand,
        'form': form,
    }
    
    return render(request, 'topressing/sand_edit.html', context)

def sandUpdate(request, pk):
    sand = SandType.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = SandTypeForm(request.POST, instance=sand)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            pending_form.save()
            
    return redirect('topd:sand_detail', pk=sand.pk)

def greensIndex(request):
    topd = GreenTopdressing.objects.all().order_by(
        '-topdress_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'topd': topd,
    }
    
    return render(request, 'topdressing/greens_index.html', context)
