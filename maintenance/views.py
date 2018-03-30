from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    Maintenance,
    OilChange,
    Repair,
    RepairPart
)

from .forms import (
    OilChangeForm,
    RepairForm,
    RepairPartForm
)

def curr_time():
    return now()

def oilchangeIndex(request):
    oilchanges = OilChange.objects.all().order_by('-updated_at')[:20]
    
    context = {
        'curr_time': curr_time(),
        'oilchanges': oilchanges,
    }
    
    return render(request, 'maintenance/oil_index.html', context)

def oilchangeNew(request):
    form = OilChangeForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'maintenance/oil_new.html', context)

def oilchangeCreate(request):
    if request.method == 'POST':
        form = OilChangeForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.total_cost = 0
            
            pending_form.save()
            form.save_m2m()
            
    return redirect('maint:oilchange_detail', pk=pending_form.pk)
                
def oilchangeDetail(request, pk):
    oilchange = OilChange.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'oilchange': oilchange,
    }
    
    return render(request, 'maintenance/oil_detail.html', context)

def oilchangeEdit(request, pk):
    oilchange = OilChange.objects.get(pk=pk)
    form = OilChangeForm(instance=oilchange)
    
    context = {
        'curr_time': curr_time(),
        'oilchange': oilchange,
        'form': form,
    }
    
    return render(request, 'maintenance/oil_edit.html', context)

def oilchangeUpdate(request, pk):
    oilchange = OilChange.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = OilChangeForm(request.POST, instance=oilchange)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
    return redirect('maint:oilchange_detail', pk=oilchange.pk)
