from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import (
    Fertilizer,
    Fertilizing,
    GreensFert,
    TeeFert,
    FairwayFert,
    RoughFert
)

from .forms import (
    FertilizerForm,
    GreensFertForm,
    TeeFertForm,
    FairwayFertForm,
    RoughFertForm
)


def curr_time():
    return now()

def index(request):

    all_fert = Fertilizing.objects.all().order_by('-fert_date')[:5]
    
    context = {
        'curr_time': curr_time(),
        'all_fert': all_fert,
    }
    return render(request, 'fertilizing/index.html', context)

def fertIndex(request):
    fertilizers = Fertilizer.objects.all().order_by('-updated_at')
    
    context = {
        'curr_time': curr_time(),
        'fertilizers': fertilizers,
    }
    
    return render(request, 'fertilizing/fert_index.html', context)

def newFert(request):
    
    form = FertilizerForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'fertilizing/newFert.html', context)

def createFert(request):
    if request.method == 'POST':
        form = FertilizerForm(data=request.POST)
        
        if form.is_valid():
            
            if request.user.is_authenticated():
                pending_form = form.save(commit=False)
                
                pending_form.unit_price = \
                    pending_form.bag_size / pending_form.price_per_bag
                
                pending_form.save()
        
    return redirect('fert:fert_detail', pk=pending_form.pk)

def fertDetail(request, pk):
    fert = Fertilizer.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'fert': fert,
    }
    
    return render(request, 'fertilizing/fert_detail.html', context)

def fertEdit(request, pk):
    fert = Fertilizer.objects.get(pk=pk)
    form = FertilizerForm(instance=fert)
    
    context = {
        'curr_time': curr_time(),
        'fert': fert,
        'form': form,
    }
    
    return render(request, 'fertilizing/fert_edit.html', context)

def fertUpdate(request, pk):
    if request.method == 'POST':
        form = FertilizerForm(data=request.POST)
        
        if form.is_valid():
            
            if request.user.is_authenticated():
                pending_form = form.save(commit=False)
    
    return redirect('fert:fert_detail', pk=pk)

def greensIndex(request):
    greens_fert = GreensFert.objects.all().order_by('-fert_date')[:10]
    
    context = {
        'curr_time': curr_time(),
        'greens_fert': greens_fert,
    }
    
    return render(request, 'fertilizing/greens_index.html', context)

def greensDetail(request, pk):
    greens_fert = GreensFert.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'greens_fert': greens_fert,
    }
    
    return render(request, 'fertilizing/greens_detail.html', context)
