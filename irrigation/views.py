from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.db.models import Q

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
    IsoSearchForm,
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
        
        if form.is_valid() and request.user.is_authenticated:
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
        
        if form.is_valid() and request.user.is_authenticated:
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
        
        if form.is_valid() and request.user.is_authenticated:
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
        
        if form.is_valid() and request.user.is_authenticated:
            form.save()
        
    return redirect('irr:sprinkler_detail', pk=sprinkler.pk)

def sprinklerSearch(request):
    if request.method == 'POST':
        return render(request, 'irrigation/sprinkler_search.html')


    else:
        searchForm = SprinklerSearchForm()

        context = {
            'curr_time': curr_time(),
            'searchForm': searchForm,
        }

        return render(request, 'irrigation/sprinkler_search.html', context)

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
        
        if form.is_valid() and request.user.is_authenticated:
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
        
        if form.is_valid() and request.user.is_authenticated:
            form.save()
    
    return redirect('irr:qc_detail', pk=qc.pk)

def drainIndex(request):
    drains = Drain.objects.all().order_by('hole_id')
    
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
        
        if form.is_valid() and request.user.is_authenticated:
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
        
        if form.is_valid() and request.user.is_authenticated:
            form.save()
            
    return redirect('irr:drain_detail', pk=drain.pk)

def isoIndex(request):
    isos = ShutoffValve.objects.all().order_by('longitude')
    
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
        
        if form.is_valid() and request.user.is_authenticated:
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
        
        if form.is_valid() and request.user.is_authenticated:
            form.save()
            
    return redirect('irr:iso_detail', pk=iso.pk)

def isoSearch(request):
    if request.method == 'GET':
        form = IsoSearchForm()

        context = {
            'curr_time': curr_time(),
            'form': form,
        }

        return render(request, 'irrigation/iso_search.html', context)

    if request.method == 'POST':
        form = IsoSearchForm(request.POST)

        is_open = True
        latitude = 0.0
        longitude = 0.0
        tee = None
        fairway = None
        green = None
        rough = None
        problem = False
        handle = ""

        if form['open'].value() == False:
            is_open = False
        if form['latitude'].value() != None:
            latitude = form['latitude'].value()
        if form['longitude'].value() != None:
            longitude = form['longitude'].value()
        if form['tee'].value() != None:
            tee = form['tee'].value()
        if form['fairway'].value() != None:
            fairway = form['fairway'].value()
        if form['green'].value() != None:
            green = form['green'].value()
        if form['rough'].value() != None:
            rough = form['rough'].value()
        if form['problem'].value() == True:
            problem = form['problem'].value()
        if form['handle'].value() != '':
            handle = form['handle'].value()

        query = """Search for iso valves where: 
                open = %s
                lat = %s
                lon = %s
                tee = %s
                fairway = %s
                green = %s
                rough = %s
                problem = %s
                handle = %s """ % (is_open,
                                 latitude,
                                 longitude,
                                 tee,
                                 fairway,
                                 green,
                                 rough,
                                 problem,
                                 handle)

        valves_open = ShutoffValve.objects.filter(Q(open=is_open))
        valves_lat = ShutoffValve.objects.filter(
                Q(latitude__icontains=latitude))
        valves_long = ShutoffValve.objects.filter(
                 Q(longitude__icontains=longitude)) 
        valves_tee = ShutoffValve.objects.filter(Q(tee=tee))
        valves_fairway = ShutoffValve.objects.filter(
                Q(fairway=fairway)) 
        valves_green = ShutoffValve.objects.filter(Q(green=green)) 
        valves_rough = ShutoffValve.objects.filter(Q(rough=rough)) 
        valves_prob = ShutoffValve.objects.filter(Q(problem=problem)) 
        valves_handle = ShutoffValve.objects.filter(
                 Q(handle__icontains=handle))

        context = {
            'curr_time': curr_time(),
            'query': query,
            'valves': valves_open,
        }

        return render(request, 'irrigation/iso_result.html', context)
                  

def digIndex(request):
    digs = IrrigationDig.objects.all().order_by('-date')
    
    context = {
        'curr_time': curr_time(),
        'digs': digs,
    }
    
    return render(request, 'irrigation/dig_index.html', context)

def digNew(request):
    form = IrrigationDigForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
    }
    
    return render(request, 'irrigation/dig_new.html', context)

def digCreate(request):
    if request.method == 'POST':
        
        form = IrrigationDigForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated:
            pending_form = form.save(commit=False)
            pending_form.save()
            
    return redirect('irr:dig_detail', pk=pending_form.pk)

def digDetail(request, pk):
    dig = IrrigationDig.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'dig': dig,
    }
    
    return render(request, 'irrigation/dig_detail.html', context)

def digEdit(request, pk):
    dig = IrrigationDig.objects.get(pk=pk)
    form = IrrigationDigForm(instance=dig)
    
    context = {
        'curr_time': curr_time(),
        'dig': dig,
        'form': form,
    }
    
    return render(request, 'irrigation/dig_edit.html', context)

def digUpdate(request, pk):
    dig = IrrigationDig.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = IrrigationDigForm(request.POST, instance=dig)
        
        if form.is_valid() and request.user.is_authenticated:
            form.save()
            
    return redirect('irr:dig_detail', pk=dig.pk)
