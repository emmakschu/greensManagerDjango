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

def qcIndex(request):
    qcs = QuickCoupler.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'qcs': qcs,
    }
    
    return render(request, 'irrigation/qc_index.html', context)

def qcNew(request):
    form = QuickCouplerForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'irrigation/qc_new.html', context)

def qcCreate(request):
    if request.method == 'POST':
        form = QuickCouplerForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
    
    return redirect('irr:qc_detail', pk=pending_form.pk)

def qcDetail(request, pk):
    qc = QuickCoupler.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'qc': qc,
    }
    
    return render(request, 'irrigation/qc_detail.html', context)

def qcEdit(request, pk):
    qc = QuickCoupler.objects.get(pk=pk)
    form = QuickCouplerForm(instance=qc)
    
    context = {
        'curr_time': curr_time(),
        'qc': qc,
        'form': form,
    }
    
    return render(request, 'irrigation/qc_edit.html', context)

def qcUpdate(request, pk):
    qc = QuickCoupler.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = QuickCouplerForm(request.POST, instance=qc)
        
        if form.is_valid() and request.user.is_authenticated():
            form.save()
    
    return redirect('irr:qc_detail', pk=qc.pk)

def drainIndex(request):
    drains = Drain.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'drains': drains,
    }
    
    return render(request, 'irrigation/drain_index.html', context)

def drainNew(request):
    form = DrainForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'irrigation/drain_new.html', context)

def drainCreate(request):
    if request.method == 'POST':
        
        form = DrainForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            
    return redirect('irr:drain_detail', pk=pending_form.pk)

def drainDetail(request, pk):
    drain = Drain.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'drain': drain,
    }
    
    return render(request, 'irrigation/drain_detail.html', context)

def drainEdit(request, pk):
    drain = Drain.objects.get(pk=pk)
    form = DrainForm(instance=drain)
    
    context = {
        'curr_time': curr_time(),
        'drain': drain,
        'form': form,
    }
    
    return render(request, 'irrigation/drain_edit.html', context)

def drainUpdate(request, pk):
    drain = Drain.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = DrainForm(request.POST, instance=drain)
        
        if form.is_valid() and request.user.is_authenticated():
            form.save()
            
    return redirect('irr:drain_detail', pk=drain.pk)

def isoIndex(request):
    isos = ShutoffValve.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'isos': isos,
    }
    
    return render(request, 'irrigation/iso_index.html', context)

def isoNew(request):
    form = ShutoffValveForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'irrigation/iso_new.html', context)

def isoCreate(request):
    if request.method == 'POST':
        
        form = ShutoffValveForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            
    return redirect('irr:iso_detail', pk=pending_form.pk)

def isoDetail(request, pk):
    iso = ShutoffValve.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'iso': iso,
    }
    
    return render(request, 'irrigation/iso_detail.html', context)

def isoEdit(request, pk):
    iso = ShutoffValve.objects.get(pk=pk)
    form = ShutoffValveForm(instance=iso)
    
    context = {
        'curr_time': curr_time(),
        'iso': iso,
        'form': form,
    }
    
    return render(request, 'irrigation/iso_edit.html', context)

def isoUpdate(request, pk):
    iso = ShutoffValve.objects.get(pk=pk)
    
    if request.method == 'POST':
        
        form = ShutoffValveForm(request.POST, instance=iso)
        
        if form.is_valid() and request.user.is_authenticated():
            form.save()
            
    return redirect('irr:iso_detail', pk=iso.pk)
