from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    Machine,
    Mower,
    GreensMower,
    TeeMower,
    FairwayMower,
    RoughMower,
    Roller,
    Aerator,
    Sprayer,
    Cart,
    TrapRake,
    UtilVehicle,
    Tractor,
    FertSpreader
)

from .forms import (
    MachineForm,
    MowerForm,
    GreensMowerForm,
    TeeMowerForm,
    FairwayMowerForm,
    RoughMowerForm,
    RollerForm,
    AeratorForm,
    SprayerForm,
    CartForm,
    TrapRakeForm,
    UtilVehicleForm,
    TractorForm,
    FertSpreaderForm
)

from maintenance import models as Maint

def curr_time():
    return now()

def index(request):
    context = {
        'curr_time': curr_time(),
    }

    return render(request, 'machines/index.html', context)

def greensmowIndex(request):
    mowers = GreensMower.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'mowers': mowers,
    }
    
    return render(request, 'machines/greensmow_index.html', context)

def greensmowNew(request):
    form = GreensMowerForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'machines/greensmow_new.html', context)

def greensmowCreate(request):
    if request.method == 'POST':
        
        form = GreensMowerForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
    
    return redirect('shop:greensmow_detail', pk=pending_form.pk)

def greensmowDetail(request, pk):
    mower = GreensMower.objects.get(pk=pk)
    oil_changes = Maint.OilChange.objects.filter(machine=mower)[:5]

    context = {
        'curr_time': curr_time(),
        'mower': mower,
        'oil_changes': oil_changes,
    }

    return render(request, 'machines/greensmow_detail.html', context)

def greensmowEdit(request, pk):
    mower = GreensMower.objects.get(pk=pk)
    form = GreensMowerForm(instance=mower)
    
    context = {
        'curr_time': curr_time(),
        'mower': mower,
        'form': form,
    }
    
    return render(request, 'machines/greensmow_edit.html', context)

def greensmowUpdate(request, pk):
    mower = GreensMower.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = GreensMowerForm(request.POST, instance=mower)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:greensmow_detail', pk=mower.pk)

def teemowIndex(request):
    mowers = TeeMower.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'mowers': mowers,
    }
    
    return render(request, 'machines/teemow_index.html', context)

def teemowNew(request):
    form = TeeMowerForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'machines/teemow_new.html', context)

def teemowCreate(request):
    if request.method == 'POST':
        
        form = TeeMowerForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
    
    return redirect('shop:teemow_detail', pk=pending_form.pk)

def teemowDetail(request, pk):
    mower = TeeMower.objects.get(pk=pk)
    oil_changes = Maint.OilChange.objects.filter(machine=mower)[:5]
    
    context = {
        'curr_time': curr_time(),
        'mower': mower,
        'oil_changes': oil_changes,
    }
    
    return render(request, 'machines/teemow_detail.html', context)

def teemowEdit(request, pk):
    mower = TeeMower.objects.get(pk=pk)
    form = TeeMowerForm(instance=mower)
    
    context = {
        'curr_time': curr_time(),
        'mower': mower,
        'form': form,
    }
    
    return render(request, 'machines/teemow_edit.html', context)

def teemowUpdate(request, pk):
    mower = TeeMower.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = TeeMowerForm(request.POST, instance=mower)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:teemow_detail', pk=mower.pk)

def fairwaymowIndex(request):
    mowers = FairwayMower.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'mowers': mowers,
    }
    
    return render(request, 'machines/fairwaymow_index.html', context)

def fairwaymowNew(request):
    form = FairwayMowerForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'machines/fairwaymow_new.html', context)

def fairwaymowCreate(request):
    if request.method == 'POST':
        
        form = FairwayMowerForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:fairwaymow_detail', pk=pending_form.pk)

def fairwaymowDetail(request, pk):
    mower = FairwayMower.objects.get(pk=pk)
    oil_changes = Maint.OilChange.objects.filter(machine=mower)[:5]
    
    context = {
        'curr_time': curr_time(),
        'mower': mower,
        'oil_changes': oil_changes,
    }
    
    return render(request, 'machines/fairwaymow_detail.html', context)

def fairwaymowEdit(request, pk):
    mower = FairwayMower.objects.get(pk=pk)
    form = FairwayMowerForm(instance=mower)
    
    context = {
        'curr_time': curr_time(),
        'mower': mower,
        'form': form,
    }
    
    return render(request, 'machines/fairwaymow_edit.html', context)

def fairwaymowUpdate(request, pk):
    mower = FairwayMower.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = FairwayMowerForm(request.POST, instance=mower)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
    
    return redirect('shop:fairwaymow_detail', pk=mower.pk)
    
    
