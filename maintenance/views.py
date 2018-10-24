from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.db.models import Q

from .models import (
    Maintenance,
    OilChange,
    Repair,
    RepairPart
)

from .forms import (
    OilChangeForm,
    RepairForm,
    RepairRequestForm,
    RepairPartForm
)

from parts.forms import PartsSearchForm

import parts.models as Parts
import machines.models as Machines

def curr_time():
    return now()
    
def partsNew(request, repair):
    repair = Maintenance.objects.get(pk=repair)
    form = RepairPartForm()
    search_form = PartsSearchForm()

    if 'filter' in request.GET:
        search_form = PartsSearchForm(request.GET)
        partNo = search_form['part_no'].value()
        make = search_form['make'].value()
        desc = search_form['description'].value()
        loc = search_form['location'].value()

        form.fields['part'].queryset = Parts.Part.objects.filter(
                (Q(part_no__icontains=partNo) |
                Q(alt_part_no__icontains=partNo)) &
                Q(make__icontains=make) &
                Q(description__icontains=desc) &
                Q(location__icontains=loc))

    if request.method == 'POST':
        form = RepairPartForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.repair_id = repair.pk

            part = Parts.Part.objects.get(pk=pending_form.part.pk)
            part.in_stock -= pending_form.qty

            added_cost = part.price * pending_form.qty
            if repair.parts_cost != None:
                repair.parts_cost += added_cost
            else:
                repair.parts_cost = added_cost
            if repair.total_cost != None:
                repair.total_cost += added_cost
            else:
                repair.total_cost = added_cost
            repair.save(update_fields=['parts_cost', 'total_cost'])
            part.save(update_fields=['in_stock',])
            pending_form.save()

    context = {
        'curr_time': curr_time(),
        'repair': repair,
        'form': form,
        'search_form': search_form,
    }

    if request.method == 'POST' and 'done' in request.POST:
        return redirect('maint:repair_detail', pk=repair.pk)
    else:
        return render(request, 'maintenance/add_repair_part.html', context)

def partsCreate(request, repair):
    repair = Maintenance.objects.get(pk=repair)
    
    if request.method == 'POST':
        form = RepairPartForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            part = Parts.Part.objects.filter(pending_form.part)
            part.in_stock -= pending_form.qty

            added_cost = part.price * pending_form.qty
            repair.parts_cost += added_cost
            repair.total_cost += added_cost

            part.save(update_fields=['in_stock',])
            repair.save(update_fields=['parts_cost', 'total_cost'])
            pending_form.save()
            
    if OilChange.objects.filter(pk=repair.pk).exists():
        return redirect('maint:oilchange_detail', pk=repair.pk)
    elif Repair.objects.filter(pk=repair.pk).exists():
        return redirect('maint:repair_detail', pk=repair.pk)

def oilchangeIndex(request):
    oilchanges = OilChange.objects.all().order_by('-date_fixed')[:20]
    
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
            
            pending_form.oil_cost = pending_form.oil.price_per_unit \
                * pending_form.oil_qty
            pending_form.total_cost = pending_form.oil_cost
            
        machine = Machines.Machine.objects.get(
            pk=pending_form.machine.pk)
        machine.hours = pending_form.hours_on_machine
        machine.save(update_fields=['hours'])
            
        pending_form.save()
        form.save_m2m()
                
    if 'done' in request.POST:
        return redirect('maint:oilchange_detail', pk=pending_form.pk)
    elif 'add_part' in request.POST:
        return redirect('maint:add_part', repair=pending_form.pk)
                
def oilchangeDetail(request, pk):
    oilchange = OilChange.objects.get(pk=pk)
    parts = RepairPart.objects.filter(repair=oilchange)
    
    context = {
        'curr_time': curr_time(),
        'oilchange': oilchange,
        'parts': parts,
    }
    
    return render(request, 'maintenance/oil_detail.html', context)

def oilchangeEdit(request, pk):
    oilchange = OilChange.objects.get(pk=pk)
    parts = RepairPart.objects.filter(repair=oilchange)
    form = OilChangeForm(instance=oilchange)
    part_forms = []
    
    for p in parts:
        part_forms.append(RepairPartForm(instance=p))
    
    context = {
        'curr_time': curr_time(),
        'oilchange': oilchange,
        'form': form,
        'part_forms': part_forms,
    }
    
    return render(request, 'maintenance/oil_edit.html', context)

def oilchangeUpdate(request, pk):
    oilchange = OilChange.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = OilChangeForm(request.POST, instance=oilchange)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.oil_cost = pending_form.oil.price_per_unit* \
                pending_form.oil_qty
            
            pending_form.total_cost = pending_form.oil_cost
            
            pending_form.save()
            form.save_m2m()
            
            for p in pending_form.parts_used.all():
                pending_form.total_cost += p.price
                
            pending_form.save()
            
    return redirect('maint:oilchange_detail', pk=oilchange.pk)

def repairIndex(request):
    repairs = Repair.objects.all().order_by('-updated_at')[:20]
    
    context = {
        'curr_time': curr_time(),
        'repairs': repairs,
    }
    
    return render(request, 'maintenance/repair_index.html', context)

def repairNew(request):
    form = RepairForm()
    part_form = RepairPartForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
        'part_form': part_form,
    }
    
    return render(request, 'maintenance/repair_new.html', context)

def repairNeeded(request, machine):
    machine = Machines.Machine.objects.get(pk=machine)
    form = RepairRequestForm(initial={
        'machine': machine,
        'acked': request.user
    })
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'maintenance/repair_needed.html', context)

def repairRequest(request):
    if request.method == 'POST':
        form = RepairRequestForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            pending_form.total_cost = 0

            machine = Machines.Machine.objects.get(
                    pk=pending_form.machine.pk)
            machine.hours = pending_form.hours_on_machine
            machine.in_commission = False
            machine.save(update_fields=['hours', 'in_commission'])

            pending_form.save()
            form.save_m2m()
            
    return redirect('maint:repair_detail', pk=pending_form.pk)

def repairCreate(request):
    if request.method == 'POST':
        form = RepairForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.total_cost = 0
            
            pending_form.save()
            form.save_m2m()
            
            if pending_form.date_fixed == None:
                machine = Machines.Machine.objects.get(
                        pk=pending_form.machine.pk)
                machine.in_commission = False
                machine.save(update_fields=['in_commission'])
                
            pending_form.save()
        
    if 'done' in request.POST:
        return redirect('maint:repair_detail', pk=pending_form.pk)
    elif 'add_part' in request.POST:
        return redirect('maint:add_part', repair=pending_form.pk)

def repairDetail(request, pk):
    if Repair.objects.filter(pk=pk).exists():
        repair = Repair.objects.get(pk=pk)
    elif OilChange.objects.filter(pk=pk).exists():
        return redirect('maint:oilchange_detail', pk=pk)
    parts = RepairPart.objects.filter(repair=repair)
    
    context = {
        'curr_time': curr_time(),
        'repair': repair,
        'parts': parts,
    }
    
    return render(request, 'maintenance/repair_detail.html', context)

def repairEdit(request, pk):
    repair = Repair.objects.get(pk=pk)
    form = RepairForm(instance=repair)
    part_form = RepairPartForm()
    
    context = {
        'curr_time': curr_time(),
        'repair': repair,
        'form': form,
        'part_form': part_form,
    }
    
    return render(request, 'maintenance/repair_edit.html', context)

def repairUpdate(request, pk):
    repair = Repair.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = RepairForm(request.POST, instance=repair)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            pending_form.save()
            
            machine = Machines.Machine.objects.get(
                pk=pending_form.machine.pk)
            
            if pending_form.date_fixed == None:
                machine.in_commission = False
            
            else:
                machine.in_commission = True
                
            machine.save(update_fields=['in_commission'])
                
            pending_form.save()

    if 'done' in request.POST:
        return redirect('maint:repair_detail', pk=pending_form.pk)
    elif 'add_part' in request.POST:
        return redirect('maint:add_part', repair=repair.pk)
            
def repairPending(request):
    repairs = Repair.objects.filter(date_fixed=None)

    context = {
        'curr_time': curr_time(),
        'repairs': repairs,
    }

    return render(request, 'maintenance/repair_pending.html', context)
