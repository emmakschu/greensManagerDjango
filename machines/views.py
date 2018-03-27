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

def roughmowIndex(request):
    mowers = RoughMower.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'mowers': mowers,
    }
    
    return render(request, 'machines/roughmow_index.html', context)

def roughmowNew(request):
    form = RoughMowerForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'machines/roughmow_new.html', context)

def roughmowCreate(request):
    if request.method == 'POST':
        
        form = RoughMowerForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:roughmow_detail', pk=pending_form.pk)

def roughmowDetail(request, pk):
    mower = RoughMower.objects.get(pk=pk)
    oil_changes = Maint.OilChange.objects.filter(machine=mower)[:5]
    
    context = {
        'curr_time': curr_time(),
        'mower': mower,
        'oil_changes': oil_changes,
    }
    
    return render(request, 'machines/roughmow_detail.html', context)

def roughmowEdit(request, pk):
    mower = RoughMower.objects.get(pk=pk)
    form = RoughMowerForm(instance=mower)
    
    context = {
        'curr_time': curr_time(),
        'mower': mower,
        'form': form,
    }
    
    return render(request, 'machines/roughmow_edit.html', context)

def roughmowUpdate(request, pk):
    mower = RoughMower.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = RoughMowerForm(request.POST, instance=mower)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:roughmow_detail', pk=mower.pk)

def getMower(request, pk):
    
    if TeeMower.objects.filter(pk=pk).exists():
        return redirect('shop:teemow_detail', pk=pk)
    elif GreensMower.objects.filter(pk=pk).exists():
        return redirect('shop:greensmow_detail', pk=pk)
    elif FairwayMower.objects.filter(pk=pk).exists():
        return redirect('shop:fairwaymow_detail', pk=pk)
    elif RoughMower.objects.filter(pk=pk).exists():
        return redirect('shop:roughmow_detail', pk=pk)
    else:
        return redirect('shop:index')

def rollerIndex(request):
    rollers = Roller.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'rollers': rollers,
    }
    
    return render(request, 'machines/roller_index.html', context)

def rollerNew(request):
    form = RollerForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'machines/roller_new.html', context)

def rollerCreate(request):
    if request.method == 'POST':
        
        form = RollerForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
    
    return redirect('shop:roller_detail', pk=pending_form.pk)

def rollerDetail(request, pk):
    roller = Roller.objects.get(pk=pk)
    oil_changes = Maint.OilChange.objects.filter(machine=roller)[:5]
    
    context = {
        'curr_time': curr_time(),
        'roller': roller,
        'oil_changes': oil_changes,
    }
    
    return render(request, 'machines/roller_detail.html', context)

def rollerEdit(request, pk):
    roller = Roller.objects.get(pk=pk)
    form = RollerForm(instance=roller)
    
    context = {
        'curr_time': curr_time(),
        'roller': roller,
        'form': form,
    }
    
    return render(request, 'machines/roller_edit.html', context)

def rollerUpdate(request, pk):
    roller = Roller.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = RollerForm(request.POST, instance=roller)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:roller_detail', pk=roller.pk)

def aeratorIndex(request):
    aerators = Aerator.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'aerators': aerators,
    }
    
    return render(request, 'machines/aerator_index.html', context)

def aeratorNew(request):
    form = AeratorForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'machines/aerator_new.html', context)

def aeratorCreate(request):
    if request.method == 'POST':
        
        form = AeratorForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:aerator_detail', pk=pending_form.pk)

def aeratorDetail(request, pk):
    aerator = Aerator.objects.get(pk=pk)
    oil_changes = Maint.OilChange.objects.filter(machine=aerator)
    
    context = {
        'curr_time': curr_time(),
        'aerator': aerator,
        'oil_changes': oil_changes,
    }
    
    return render(request, 'machines/aerator_detail.html', context)

def aeratorEdit(request, pk):
    aerator = Aerator.objects.get(pk=pk)
    form = AeratorForm(instance=aerator)
    
    context = {
        'curr_time': curr_time(),
        'aerator': aerator,
        'form': form,
    }
    
    return render(request, 'machines/aerator_edit.html', context)

def aeratorUpdate(request, pk):
    aerator = Aerator.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = AeratorForm(request.POST, instance=aerator)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:aerator_detail', pk=aerator.pk)

def sprayerIndex(request):
    sprayers = Sprayer.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'sprayers': sprayers,
    }
    
    return render(request, 'machines/sprayer_index.html', context)

def sprayerNew(request):
    form = SprayerForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'machines/sprayer_new.html', context)

def sprayerCreate(request):
    if request.method == 'POST':
        form = SprayerForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:sprayer_detail', pk=pending_form.pk)

def sprayerDetail(request, pk):
    sprayer = Sprayer.objects.get(pk=pk)
    oil_changes = Maint.OilChange.objects.filter(machine=sprayer)[:5]
    
    context = {
        'curr_time': curr_time(),
        'sprayer': sprayer,
        'oil_changes': oil_changes,
    }
    
    return render(request, 'machines/sprayer_detail.html', context)

def sprayerEdit(request, pk):
    sprayer = Sprayer.objects.get(pk=pk)
    form = SprayerForm(instance=sprayer)
    
    context = {
        'curr_time': curr_time(),
        'sprayer': sprayer,
        'form': form,
    }
    
    return render(request, 'machines/sprayer_edit.html', context)

def sprayerUpdate(request, pk):
    sprayer = Sprayer.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = SprayerForm(request.POST, instance=sprayer)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:sprayer_detail', pk=sprayer.pk)

def cartIndex(request):
    carts = Cart.objects.all()
    
    context = {
        'curr_time': curr_time(),
        'carts': carts,
    }
    
    return render(request, 'machines/cart_index.html', context)

def cartNew(request):
    form = CartForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'machines/cart_new.html', context)

def cartCreate(request):
    if request.method == 'POST':
        
        form = CartForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:cart_detail', pk=pending_form.pk)

def cartDetail(request, pk):
    cart = Cart.objects.get(pk=pk)
    oil_changes = Maint.OilChange.objects.filter(machine=cart)
    
    context = {
        'curr_time': curr_time(),
        'cart': cart,
        'oil_changes': oil_changes,
    }
    
    return render(request, 'machines/cart_detail.html', context)

def cartEdit(request, pk):
    cart = Cart.objects.get(pk=pk)
    form = CartForm(instance=cart)
    
    context = {
        'curr_time': curr_time(),
        'cart': cart,
        'form': form,
    }
    
    return render(request, 'machines/cart_edit.html', context)

def cartUpdate(request, pk):
    cart = Cart.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = CartForm(request.POST, instance=cart)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.save()
            form.save_m2m()
            
    return redirect('shop:cart_detail', pk=cart.pk)
