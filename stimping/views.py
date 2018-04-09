rom django.shortcuts import render, redirect
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
    
    return render(request, 'stimping/index.html', context)

def new(request):
    form = StimpForm()
    simpleForm = SimpleStimpForm()
    
    context = {
        'curr_time': curr_time(),
        'form': form,
        'simpleForm': simpleForm,
    }
    
    return render(request, 'stimping/new.html', context)

def create(request):
    if request.method == 'POST':
        form = StimpForm(data=request.POST)
        
        if form.is_valid() and request.user.is_authenticated():
            pending_form = form.save(commit=False)
            
            if pending_form.simple_version:
                for f in (pending_form.forward2, 
                          pending_form.forward3):
                    f = pending_form.forward1
                
                for f in (pending_form.backward2,
                          pending_form.backward3):
                    f = pending_form.backward1
                    
                for f in (pending_form.left2,
                          pending_form.left3):
                    f = pending_form.left1
                    
                for f in (pending_form.right2,
                          pending_form.right3):
                    f = pending_form.right1
                    
            pending_form.forward_avg = s.list_mean(
                [pending_form.forward1, pending_form.forward2,
                    pending_form.forward3])
            pending_form.backward_avg = s.list_mean(
                [pending_form.backward1, pending_form.backward2,
                    pending_form.backward3])
            pending_form.left_avg = s.list_mean(
                [pending_form.left1, pending_form.left2,
                    pending_form.left3])
            pending_form.right_avg = s.list_mean(
                [pending_form.right1, pending_form.right2,
                    pending_form.right3])
            
            all_vals = [
                pending_form.forward1,
                pending_form.forward2,
                pending_form.forward3,
                pending_form.backward1,
                pending_form.backward2,
                pending_form.backward3,
                pending_form.left1,
                pending_form.left2,
                pending_form.left3,
                pending_form.right1,
                pending_form.right2,
                pending_form.right3 
            ]
            
            pending_form.raw_speed = s.list_mean(
                [pending_form.forward_avg, pending_form.backward_avg,
                 pending_form.left_avg, pending_form.right_avg])
            
            pending_form.adj_speed = s.stimp_two_axes_adjusted(
                all_vals[0],
                all_vals[1],
                all_vals[2],
                all_vals[3],
                all_vals[4],
                all_vals[5],
                all_vals[6],
                all_vals[7],
                all_vals[8],
                all_vals[9],
                all_vals[10],
                all_vals[11])
            
            pending_form.mu_k = s.get_friction_coeff(
                pending_form.adj_speed)
            
            pending_form.stdDev = s.list_std_dev(all_vals)
            
            pending_form.save()
            
    return redirect('stimp:detail', pk=pending_form.pk)
        
def detail(request, pk):
    stimp = Stimp.objects.get(pk=pk)
    
    context = {
        'curr_time': curr_time(),
        'stimp': stimp,
    }
    
    return render(request, 'stimping/detail.html', context)
