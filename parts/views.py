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

def partIndex(request):
    parts = Part.objects.all().order_by('-updated_at')[:40]
    
    context = {
        'curr_time': curr_time(),
        'parts': parts,
    }
    
    return render(request, 'parts/part_index.html', context)

def partNew(request):
    form = PartForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'parts/part_new.html', context)

def partCreate(request):
    if request.method == 'POST':
        form = PartForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
        
    return redirect('parts:part_detail', pk=pending_form.pk)

def partDetail(request, pk):
    part = Part.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'part': part,
    }
    
    return render(request, 'parts/part_detail.html', context)

def partEdit(request, pk):
    part = Part.objects.get(pk=pk)
    form = PartForm(instance=part)
    
    context = {
        'curr_time': curr_time(),
        'part': part,
        'form': form,
    }
    
    return render(request, 'parts/part_edit.html', context)

def partUpdate(request, pk):
    part = Part.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = PartForm(request.POST, instance=part)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            
    return redirect('parts:part_detail', pk=part.pk)

def filterIndex(request):
    filters = Filter.objects.all().order_by('-updated_at')[:20]
    
    context = {
        'curr_time': curr_time(),
        'filters': filters,
    }
    
    return render(request, 'parts/filter_index.html', context)

def filterNew(request):
    form = FilterForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'parts/filter_new.html', context)

def filterCreate(request):
    if request.method == 'POST':
        
        form = FilterForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            
    return redirect('parts:filter_detail', pk=pending_form.pk)

def filterDetail(request, pk):
    filt = Filter.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'filter': filt,
    }
    
    return render(request, 'parts/filter_detail.html', context)

def filterEdit(request, pk):
    filt = Filter.objects.get(pk=pk)
    form = FilterForm(instance=filt)
    
    context = {
        'curr_time': curr_time(),
        'filter': filt,
        'form': form,
    }
    
    return render(request, 'parts/filter_edit.html', context)

def filterUpdate(request, pk):
    filt = Filter.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = FilterForm(request.POST, instance=filt)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
    
    return redirect('parts:filter_detail', pk=filt.pk)
