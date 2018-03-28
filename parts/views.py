from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    Fluid,
    Fuel,
    Oil,
    Part,
    Filter
)

from .forms import (
    FuelForm,
    OilForm,
    PartForm,
    FilterForm
)

def curr_time():
    return now()

def index(request):
    recently_added = \
        Part.objects.all().order_by('-created_at')[:10]
    recently_updated = \
        Part.objects.all().order_by('-updated_at')[:10]
    oos = \
        Part.objects.filter(in_stock=0).order_by('-updated_at')[:10]

    context = {
        'curr_time': curr_time(),
        'recently_added': recently_added,
        'recently_updated': recently_updated,
        'oos': oos,
    }

    return render(request, 'parts/index.html', context)

def fuelIndex(request):
    fuels = Fuel.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'fuels': fuels,
    }
    
    return render(request, 'parts/fuel_index.html', context)

def fuelNew(request):
    form = FuelForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'parts/fuel_new.html', context)

def fuelCreate(request):
    if request.method == 'POST':
        
        form = FuelForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            unit_price = pending_form.price / pending_form.unit_size
            pending_form.price_per_unit = unit_price
            pending_form.save()
            
    return redirect('parts:fuel_detail', pk=pending_form.pk)

def fuelDetail(request, pk):
    fuel = Fuel.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'fuel': fuel,
    }
    
    return render(request, 'parts/fuel_detail.html', context)

def fuelEdit(request, pk):
    fuel = Fuel.objects.get(pk=pk)
    form = FuelForm(instance=fuel)
    
    context = {
        'curr_time': curr_time(),
        'fuel': fuel,
        'form': form,
    }
    
    return render(request, 'parts/fuel_edit.html', context)

def fuelUpdate(request, pk):
    fuel = Fuel.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = FuelForm(request.POST, instance=fuel)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            unit_price = pending_form.price / pending_form.unit_size
            pending_form.price_per_unit = unit_price
            pending_form.save()
            
    return redirect('parts:fuel_detail', pk=fuel.pk)

def oilIndex(request):
    oils = Oil.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'oils': oils,
    }
    
    return render(request, 'parts/oil_index.html', context)

def oilNew(request):
    form = OilForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'parts/oil_new.html', context)

def oilCreate(request):
    if request.method == 'POST':
        
        form = OilForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            unit_price = pending_form.price / pending_form.unit_size
            pending_form.price_per_unit = unit_price
            pending_form.save()
            
    return redirect('parts:oil_detail', pk=pending_form.pk)

def oilDetail(request, pk):
    oil = Oil.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'oil': oil,
    }
    
    return render(request, 'parts/oil_detail.html', context)

def oilEdit(request, pk):
    oil = Oil.objects.get(pk=pk)
    form = OilForm(instance=oil)
    
    context = {
        'curr_time': curr_time(),
        'oil': oil,
        'form': form,
    }
    
    return render(request, 'parts/oil_edit.html', context)

def oilUpdate(request, pk):
    oil = Oil.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = OilForm(request.POST, instance=oil)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            unit_price = pending_form.price / pending_form.unit_size
            pending_form.price_per_unit = unit_price
            pending_form.save()
            
    return redirect('parts:oil_detail', pk=oil.pk)
