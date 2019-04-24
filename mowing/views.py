from django.shortcuts import render, redirect
from django.utils.timezone import now

import math
from decimal import Decimal

from courses import models as Courses
from fertilizing import models as Fert
from irrigation import models as Irrig
from machines import models as Machines
from parts import models as Parts
from turfs import models as Turfs
from rolling import models as Roll

from .models import (
    Mowing,
    GreensMowing,
    TeeMowing,
    FairwayMowing,
    RoughMowing
)

from .forms import (
    GreensMowingForm,
    TeeMowingForm,
    FairwayMowingForm,
    RoughMowingForm
)

PI = Decimal(math.pi)

def curr_time():
    return now()

def index(request):
    curr_time = now()
    greens_mow = \
        GreensMowing.objects.all().order_by('-mow_date')[:5]
    last_greens = curr_time - greens_mow.first().mow_date
    last_greens = "%d days, %02d:%02d" % (
        last_greens.days,
        last_greens.seconds / 3600,
        (last_greens.seconds / 60) % 60
    )

    tee_mow = \
        TeeMowing.objects.all().order_by('-mow_date')[:5]
    last_tees = curr_time - tee_mow.first().mow_date
    last_tees = "%d days, %02d:%02d" % (
        last_tees.days,
        last_tees.seconds / 3600,
        (last_tees.seconds / 60) % 60
    )

    fairway_mow = \
        FairwayMowing.objects.all().order_by('-mow_date')[:5]
    last_fairway = curr_time - fairway_mow.first().mow_date
    last_fairway = "%d days, %02d:%02d" % (
        last_fairway.days,
        last_fairway.seconds / 3600,
        (last_fairway.seconds / 60) % 60
    )

    rough_mow = \
        RoughMowing.objects.all().order_by('-mow_date')[:5]
    last_rough = curr_time - rough_mow.first().mow_date
    last_rough = "%d days, %02d:%02d" % (
        last_rough.days,
        last_rough.seconds / 3600,
        (last_rough.seconds / 60) % 60
    )

    context = {
        'curr_time': curr_time,
        'greens_mow': greens_mow,
        'last_greens': last_greens,
        'tee_mow': tee_mow,
        'last_tees': last_tees,
        'fairway_mow': fairway_mow,
        'last_fairway': last_fairway,
        'rough_mow': rough_mow,
        'last_rough': last_rough
    }

    return render(request, 'mowing/index.html', context)

def greensIndex(request):
    mowings = GreensMowing.objects.all().order_by('-mow_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'mowings': mowings,
    }
    
    return render(request, 'mowing/greens_index.html', context)

def greensNew(request):
    form = GreensMowingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'mowing/greens_new.html', context)

def greensCreate(request):
    if request.method == 'POST':
        form = GreensMowingForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
            for g in pending_form.green.all():
                green = Courses.Green.objects.get(pk=g.pk)
                green.mow_direction += PI / 4
                if green.mow_direction >= PI:
                    green.mow_direction -= PI
                green.save()
            
    return redirect('mow:greens_detail', pk=pending_form.pk)

def greensDetail(request, pk):
    mowing = GreensMowing.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'mowing': mowing,
    }
    
    return render(request, 'mowing/greens_detail.html', context)

def greensEdit(request, pk):
    mowing = GreensMowing.objects.get(pk=pk)
    form = GreensMowingForm(instance=mowing)
    
    context = {
        'curr_time': curr_time(),
        'mowing': mowing,
        'form': form,
    }
    
    return render(request, 'mowing/greens_edit.html', context)

def greensUpdate(request, pk):
    mowing = GreensMowing.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = GreensMowingForm(request.POST, instance=mowing)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('mow:greens_detail', pk=mowing.pk)

def teesIndex(request):
    mowings = TeeMowing.objects.all().order_by('-mow_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'mowings': mowings,
    }
    
    return render(request, 'mowing/tees_index.html', context)

def teesNew(request):
    form = TeeMowingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'mowing/tees_new.html', context)

def teesCreate(request):
    if request.method == 'POST':
        form = TeeMowingForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('mow:tees_detail', pk=pending_form.pk)

def teesDetail(request, pk):
    mowing = TeeMowing.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'mowing': mowing,
    }
    
    return render(request, 'mowing/tees_detail.html', context)

def teesEdit(request, pk):
    mowing = TeeMowing.objects.get(pk=pk)
    form = TeeMowingForm(instance=mowing)
    
    context = {
        'curr_time': curr_time(),
        'mowing': mowing,
        'form': form,
    }
    
    return render(request, 'mowing/tees_edit.html', context)

def teesUpdate(request, pk):
    mowing = TeeMowing.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = TeeMowingForm(request.POST, instance=mowing)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
    
    return redirect('mow:tees_detail', pk=mowing.pk)

def fairwaysIndex(request):
    mowings = FairwayMowing.objects.all().order_by('-mow_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'mowings': mowings,
    }
    
    return render(request, 'mowing/fairways_index.html', context)

def fairwaysNew(request):
    form = FairwayMowingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'mowing/fairways_new.html', context)

def fairwaysCreate(request):
    if request.method == 'POST':
        form = FairwayMowingForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('mow:fairways_detail', pk=pending_form.pk)

def fairwaysDetail(request, pk):
    mowing = FairwayMowing.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'mowing': mowing,
    }
    
    return render(request, 'mowing/fairways_detail.html', context)

def fairwaysEdit(request, pk):
    mowing = FairwayMowing.objects.get(pk=pk)
    form = FairwayMowingForm(instance=mowing)
    
    context = {
        'curr_time': curr_time(),
        'mowing': mowing,
        'form': form,
    }
    
    return render(request, 'mowing/fairways_edit.html', context)

def fairwaysUpdate(request, pk):
    mowing = FairwayMowing.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = FairwayMowingForm(request.POST, instance=mowing)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('mow:fairways_detail', pk=mowing.pk)

def roughsIndex(request):
    mowings = RoughMowing.objects.all().order_by('-mow_date')[:20]
    
    context = {
        'curr_time': curr_time(),
        'mowings': mowings,
    }
    
    return render(request, 'mowing/roughs_index.html', context)

def roughsNew(request):
    form = RoughMowingForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'mowing/roughs_new.html', context)

def roughsCreate(request):
    if request.method == 'POST':
        form = RoughMowingForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('mow:roughs_detail', pk=pending_form.pk)

def roughsDetail(request, pk):
    mowing = RoughMowing.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'mowing': mowing,
    }
    
    return render(request, 'mowing/roughs_detail.html', context)

def roughsEdit(request, pk):
    mowing = RoughMowing.objects.get(pk=pk)
    form = RoughMowingForm(instance=mowing)
    
    context = {
        'curr_time': curr_time(),
        'mowing': mowing,
        'form': form,
    }
    
    return render(request, 'mowing/roughs_edit.html', context)

def roughsUpdate(request, pk):
    mowing = RoughMowing.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = RoughMowingForm(request.POST, instance=mowing)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('mow:roughs_detail', pk=mowing.pk)
