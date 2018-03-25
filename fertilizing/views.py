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
    
    return render(request, 'fertilizing/fert_new.html', context)

def createFert(request):
    if request.method == 'POST':
        form = FertilizerForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
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
    fert = Fertilizer.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = FertilizerForm(instance=fert, data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.unit_price = \
                pending_form.bag_size / pending_form.price_per_bag
            
            pending_form.save()
    
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

def greensNew(request):
    form = GreensFertForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'fertilizing/greens_new.html', context)

def greensCreate(request):
    if request.method == 'POST':
        form = GreensFertForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            price_per_bag = pending_form.fertilizer.price_per_bag
            pending_form.cost = pending_form.bags_used * price_per_bag
            
            pending_form.save()
            form.save_m2m()
                
    return redirect('fert:greens_detail', pk=pending_form.pk)

def greensEdit(request, pk):
    greens_fert = GreensFert.objects.get(pk=pk)
    
    form = GreensFertForm(instance=greens_fert)
    
    context = {
        'curr_time': curr_time(),
        'greens_fert': greens_fert,
        'form': form,
    }
    
    return render(request, 'fertilizing/greens_edit.html', context)

def greensUpdate(request, pk):
    greens_fert = GreensFert.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = GreensFertForm(request.POST, instance=greens_fert)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            price_per_bag = pending_form.fertilizer.price_per_bag
            pending_form.cost = pending_form.bags_used * price_per_bag
            
            form.save_m2m()
        
    return redirect('fert:greens_detail', pk=pending_form.pk)
            
def teesIndex(request):
    tees_fert = TeeFert.objects.all().order_by('-fert_date')[:10]
    
    context = {
        'curr_time': curr_time(),
        'tees_fert': tees_fert,
    }
    
    return render(request, 'fertilizing/tees_index.html', context)

def teesDetail(request, pk):
    tees_fert = TeeFert.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'tees_fert': tees_fert,
    }
    
    return render(request, 'fertilizing/tees_detail.html', context)

def teesNew(request):
    form = TeeFertForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'fertilizing/tees_new.html', context)

def teesCreate(request):
    if request.method == 'POST':
        form = TeeFertForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            price_per_bag = pending_form.fertilizer.price_per_bag
            pending_form.cost = pending_form.bags_used * price_per_bag
            
            pending_form.save()
            form.save_m2m()
                
    return redirect('fert:tees_detail', pk=pending_form.pk)

def teesEdit(request, pk):
    tees_fert = TeeFert.objects.get(pk=pk)
    
    form = TeeFertForm(instance=tees_fert)
    
    context = {
        'curr_time': curr_time(),
        'tees_fert': tees_fert,
        'form': form,
    }
    
    return render(request, 'fertilizing/tees_edit.html', context)

def teesUpdate(request, pk):
    tees_fert = TeeFert.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = TeeFertForm(request.POST, instance=tees_fert)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            price_per_bag = pending_form.fertilizer.price_per_bag
            pending_form.cost = pending_form.bags_used * price_per_bag
            
            form.save_m2m()
        
    return redirect('fert:tees_detail', pk=pending_form.pk)

def fairwaysIndex(request):
    fairways_fert = FairwayFert.objects.all().order_by('-fert_date')[:10]
    
    context = {
        'curr_time': curr_time(),
        'fairways_fert': fairways_fert,
    }
    
    return render(request, 'fertilizing/fairways_index.html', context)

def fairwaysDetail(request, pk):
    fairways_fert = FairwayFert.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'fairways_fert': fairways_fert,
    }
    
    return render(request, 'fertilizing/fairways_detail.html', context)

def fairwaysNew(request):
    form = FairwayFertForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'fertilizing/fairways_new.html', context)

def fairwaysCreate(request):
    if request.method == 'POST':
        form = FairwayFertForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            price_per_bag = pending_form.fertilizer.price_per_bag
            pending_form.cost = pending_form.bags_used * price_per_bag
            
            pending_form.save()
            form.save_m2m()
                
    return redirect('fert:fairways_detail', pk=pending_form.pk)

def fairwaysEdit(request, pk):
    fairways_fert = FairwayFert.objects.get(pk=pk)
    
    form = FairwayFertForm(instance=fairways_fert)
    
    context = {
        'curr_time': curr_time(),
        'fairways_fert': fairways_fert,
        'form': form,
    }
    
    return render(request, 'fertilizing/fairways_edit.html', context)

def fairwaysUpdate(request, pk):
    fairways_fert = FairwayFert.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = FairwayFertForm(request.POST, instance=fairways_fert)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            price_per_bag = pending_form.fertilizer.price_per_bag
            pending_form.cost = pending_form.bags_used * price_per_bag
            
            form.save_m2m()
        
    return redirect('fert:fairways_detail', pk=pending_form.pk)

def roughsIndex(request):
    roughs_fert = RoughFert.objects.all().order_by('-fert_date')[:10]
    
    context = {
        'curr_time': curr_time(),
        'roughs_fert': roughs_fert,
    }
    
    return render(request, 'fertilizing/roughs_index.html', context)

def roughsDetail(request, pk):
    roughs_fert = RoughFert.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'roughs_fert': roughs_fert,
    }
    
    return render(request, 'fertilizing/roughs_detail.html', context)

def roughsNew(request):
    form = RoughFertForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'fertilizing/roughs_new.html', context)

def roughsCreate(request):
    if request.method == 'POST':
        form = RoughFertForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            price_per_bag = pending_form.fertilizer.price_per_bag
            pending_form.cost = pending_form.bags_used * price_per_bag
            
            pending_form.save()
            form.save_m2m()
                
    return redirect('fert:roughs_detail', pk=pending_form.pk)

def roughsEdit(request, pk):
    roughs_fert = RoughFert.objects.get(pk=pk)
    
    form = RoughFertForm(instance=roughs_fert)
    
    context = {
        'curr_time': curr_time(),
        'roughs_fert': roughs_fert,
        'form': form,
    }
    
    return render(request, 'fertilizing/roughs_edit.html', context)

def roughsUpdate(request, pk):
    roughs_fert = RoughFert.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = RoughFertForm(request.POST, instance=roughs_fert)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            price_per_bag = pending_form.fertilizer.price_per_bag
            pending_form.cost = pending_form.bags_used * price_per_bag
            
            form.save_m2m()
        
    return redirect('fert:roughs_detail', pk=pending_form.pk)
