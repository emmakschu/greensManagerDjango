from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    SatelliteBox,
    SprinklerHead,
    QuickCoupler,
    Drain,
    ShutoffValve,
    IrrigationDig
)

from .forms import (
    SatelliteBoxForm,
    SprinklerHeadForm,
    QuickCouplerForm,
    DrainForm,
    ShutoffValveForm,
    IrrigationDigForm
)

def curr_time():
    return now()

def index(request):
    return render(request, 'irrigation/index.html')

def satboxIndex(request):
    satboxes = SatelliteBox.objects.all().order_by('box_number')
    
    context = {
        'curr_time': curr_time(),
        'satboxes': satboxes,
    }
    
    return render(request, 'irrigation/satbox_index.html', context)

def satboxNew(request):
    form = SatelliteBoxForm()
    
    context = {
        'curr_time': curr_time,
        'form': form,
    }
    
    return render(request, 'irrigation/satbox_new.html', context)

def satboxCreate(request):
    if request.method == 'POST':
        form = SatelliteBoxForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
    
    return redirect('irr:satbox_detail', pk=pending_form.pk)

def satboxDetail(request, pk):
    satbox = SatelliteBox.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time,
        'satbox': satbox,
    }
    
    return render(request, 'irrigation/satbox_detail.html', context)

def satboxEdit(request, pk):
    satbox = SatelliteBox.objects.get(pk=pk)
    form = SatelliteBoxForm(instance=satbox)
    
    context = {
        'curr_time': curr_time,
        'satbox': satbox,
        'form': form,
    }
    
    return render(request, 'irrigation/satbox_edit.html', context)

def satboxUpdate(request, pk):
    satbox = SatelliteBox.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = SatelliteBoxForm(request.POST, instance=satbox)
        
        if form.is_valid() and request.user.is_authenticated():
            form.save()
        
    return redirect('irr:satbox_detail', pk=satbox.pk)

def sprinklerIndex(request):
    sprinklers = SprinklerHead.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'sprinklers': sprinklers,
    }
    
    return render(request, 'irrigation/sprinkler_index.html', context)

def sprinklerNew(request):
    form = SprinklerHeadForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'irrigation/sprinkler_new.html', context)

def sprinklerCreate(request):
    if request.method == 'POST':
        form = SprinklerHeadForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            
    return redirect('irr:sprinkler_detail', pk=pending_form.pk)

def sprinklerDetail(request, pk):
    sprinkler = SprinklerHead.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'sprinkler': sprinkler,
    }
    
    return render(request, 'irrigation/sprinkler_detail.html',
                  context)

def sprinklerEdit(request, pk):
    sprinkler = SprinklerHead.objects.get(pk=pk)
    form = SprinklerHeadForm(instance=sprinkler)
    
    context = {
        'curr_time': curr_time(),
        'sprinkler': sprinkler,
        'form': form,
    }
    
    return render(request, 'irrigation/sprinkler_edit.html', context)

def sprinklerUpdate(request, pk):
    sprinkler = SprinklerHead.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = SprinklerHeadForm(request.POST, instance=sprinkler)
        
        if form.is_valid() and request.user.is_authenticated():
            form.save()
        
    return redirect('irr:sprinkler_detail', pk=sprinkler.pk)
