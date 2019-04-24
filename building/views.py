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

from courses.models import (
    Green,
    Tee,
    Fairway 
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
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            green = Green.objects.get(pk=pending_form.green.pk)
            green.soil_type = pending_form.soil_type
            
            if pending_form.cultivar != None:
                cult = \
                    Cultivar.objects.get(pk=pending_form.cultivar.pk) 
                pending_form.species = cult.species 
                green.turf_cultivar = pending_form.cultivar
                
            green.turf_species = pending_form.species
            green.save()
            
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
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            green = Green.objects.get(pk=pending_form.green.pk)
            green.soil_type = pending_form.soil_type
            
            if pending_form.cultivar != None:
                cult = \
                    Cultivar.objects.get(pk=pending_form.cultivar.pk) 
                pending_form.species = cult.species 
                green.turf_cultivar = pending_form.cultivar
                
            green.turf_species = pending_form.species
            green.save()
            
            pending_form.save()
            
    return redirect('build:green_detail', pk=pending_form.pk)

def teeIndex(request):
    builds = BuildTee.objects.all().order_by('-build_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'builds': builds,
    }
    
    return render(request, 'building/tee_index.html', context)

def teeNew(request):
    form = BuildTeeForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'building/tee_new.html', context)

def teeCreate(request):
    if request.method == 'POST':
        form = BuildTeeForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            tee = Tee.objects.get(pk=pending_form.tee.pk)
            tee.soil_type = pending_form.soil_type
            
            if pending_form.cultivar != None:
                cult = \
                    Cultivar.objects.get(pk=pending_form.cultivar.pk)
                pending_form.species = cult.species
                tee.turf_cultivar = pending_form.cultivar
                
            tee.turf_species = pending_form.species
            tee.save()
                
            pending_form.save()
            
    return redirect('build:tee_detail', pk=pending_form.pk)

def teeDetail(request, pk):
    build = BuildTee.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'build': build,
    }
    
    return render(request, 'building/tee_detail.html', context)

def teeEdit(request, pk):
    build = BuildTee.objects.get(pk=pk)
    form = BuildTeeForm(instance=build)
    
    context = {
        'curr_time': curr_time(),
        'build': build,
        'form': form,
    }
    
    return render(request, 'building/tee_edit.html', context)

def teeUpdate(request, pk):
    build = BuildTee.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = BuildTeeForm(request.POST, instance=build)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            tee = Tee.objects.get(pk=pending_form.tee.pk)
            tee.soil_type = pending_form.soil_type
            
            if pending_form.cultivar != None:
                cult = \
                    Cultivar.objects.get(pk=pending_form.cultivar.pk)
                pending_form.species = cult.species
                tee.turf_cultivar = pending_form.cultivar
                
            tee.turf_species = pending_form.species
            tee.save()
                
            pending_form.save()
            
    return redirect('build:tee_detail', pk=build.pk)

def fairwayIndex(request):
    builds = BuildFairway.objects.all().order_by('-build_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'builds': builds,
    }
    
    return render(request, 'building/fairway_index.html', context)

def fairwayNew(request):
    form = BuildFairwayForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'building/fairway_new.html', context)

def fairwayCreate(request):
    if request.method == 'POST':
        form = BuildFairwayForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            fairway = Fairway.objects.get(pk=pending_form.fairway.pk)
            
            if pending_form.soil_type != None:
                fairway.soil_type = pending_form.soil_type
            
            if pending_form.cultivar != None:
                cult = \
                    Cultivar.objects.get(pk=pending_form.cultivar.pk)
                pending_form.species = cult.species
                
                fairway.turf_cultivar = pending_form.cultivar
                
            if pending_form.species != None:
                fairway.turf_species = pending_form.species
                
            fairway.save()
            
            pending_form.save()
            
    return redirect('build:fairway_detail', pk=pending_form.pk)

def fairwayDetail(request, pk):
    build = BuildFairway.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'build': build,
    }
    
    return render(request, 'building/fairway_detail.html', context)

def fairwayEdit(request, pk):
    build = BuildFairway.objects.get(pk=pk)
    form = BuildFairwayForm(instance=build)
    
    context = {
        'curr_time': curr_time(),
        'build': build,
        'form': form,
    }
    
    return render(request, 'building/fairway_edit.html', context)

def fairwayUpdate(request, pk):
    build = BuildFairway.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = BuildFairwayForm(request.POST, instance=build)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            fairway = Fairway.objects.get(pk=pending_form.fairway.pk)
            
            if pending_form.soil_type != None:
                fairway.soil_type = pending_form.soil_type
            
            if pending_form.cultivar != None:
                cult = \
                    Cultivar.objects.get(pk=pending_form.cultivar.pk)
                pending_form.species = cult.species
                
                fairway.turf_cultivar = pending_form.cultivar
                
            if pending_form.species != None:
                fairway.turf_species = pending_form.species
                
            fairway.save()
            
            pending_form.save()
            
    return redirect('build:fairway_detail', pk=build.pk)

def bunkerIndex(request):
    builds = BuildBunker.objects.all().order_by('-build_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'builds': builds,
    }
    
    return render(request, 'building/bunker_index.html', context)

def bunkerNew(request):
    form = BuildBunkerForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'building/bunker_new.html', context)

def bunkerCreate(request):
    if request.method == 'POST':
        form = BuildBunkerForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            
    return redirect('build:bunker_detail', pk=pending_form.pk)

def bunkerDetail(request, pk):
    build = BuildBunker.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'build': build,
    }
    
    return render(request, 'building/bunker_detail.html', context)

def bunkerEdit(request, pk):
    build = BuildBunker.objects.get(pk=pk)
    form = BuildBunkerForm(instance=build)
    
    context = {
        'curr_time': curr_time(),
        'build': build,
        'form': form,
    }
    
    return render(request, 'building/bunker_edit.html', context)

def bunkerUpdate(request, pk):
    build = BuildBunker.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = BuildBunkerForm(request.POST, instance=build)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            
    return redirect('build:bunker_detail', pk=build.pk)
