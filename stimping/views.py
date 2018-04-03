from django.shortcuts import render, redirect
from django.utils.timezone import now

from .models import Stimp
from .forms import StimpForm, SimpleStimpForm
import stimp as s

def curr_time():
    return now()

def index(request):
    stimps = Stimp.objects.all().order_by('-created_at')[:20]
    
    context = {
        'curr_time': curr_time(),
        'stimps': stimps,
    }
    
    return render(request, 'stimps/index.html', context)

def new(request):
    form = StimpForm()
    simpleForm = SimpleStimpForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
        'simpleForm': simpleForm,
    }
    
    return render(request, 'stimps/new.html', context)

def create(request):
    if request.method == 'POST':
        form = StimpForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            if pending_form.simple_version:
                pending_form.forward_avg = pending_form.forward1
                pending_form.backward_avg = pending_form.backward1
                pending_form.left_avg = pending_form.left1
                pending_form.right_avg = pending_form.right1
            
            
    return redirect('stimp:detail', pk=pending_form.pk)
        
