from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    BuildGreen,
    BuildTee,
    BuildFairway,
    BuildBunker
)

from .forms import (
    BuildGreenForm,
    BuildTeeForm,
    BuildFairwayForm,
    BuildBunkerForm
)

from turfs.models import (
    TurfgrassSpecies,
    Cultivar
)

def curr_time():
    return now()

def greenIndex(request):
    builds = BuildGreen.objects.all().order_by('-build_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'builds': builds,
    }
    
    return render(request, 'building/green_index.html', context)

def greenNew(request):
    form = BuildGreenForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'building/green_new.html', context)

def greenCreate(request):
    if request.method == 'POST':
        form = BuildGreenForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            if pending_form.cultivar != None:
                cult = \
                    Cultivar.objects.get(pk=pending_form.cultivar.pk) 
                pending_form.species = cult.species 
            pending_form.save()
            
    return redirect('build:green_detail', pk=pending_form.pk)

def greenDetail(request, pk):
    build = BuildGreen.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'build': build,
    }
    
    return render(request, 'building/green_detail.html', context)

def greenEdit(request, pk):
    build = BuildGreen.objects.get(pk=pk)
    form = BuildGreenForm(instance=build)
    
    context = {
        'curr_time': curr_time(),
        'build': build,
        'form': form,
    }
    
    return render(request, 'building/green_edit.html', context)

def greenUpdate(request, pk):
    build = BuildGreen.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = BuildGreenForm(request.POST, instance=build)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            if pending_form.cultivar != None:
                cult = \
                    Cultivar.objects.get(pk=pending_form.cultivar.pk)
                pending_form.species = cult.species
                
            pending_form.save()
            
    return redirect('build:green_detail', pk=pending_form.pk)
