from django.shortcuts import render, redirect
from django.utils.timezone import now

from courses.models import (
    Course,
    Hole,
    Tee,
    Green,
    Fairway,
    Bunker
)

def curr_time():
    return now()

def index(request):
    courses = Course.objects.all()
    holes = Hole.objects.all()

    context = {
        'curr_time': curr_time(),
        'courses': courses,
        'holes': holes,
    }
    return render(request, 'courses/index.html', context)

def course_detail(request, pk):
    course = Course.objects.prefetch_related(
        'hole', 'hole__green', 'hole__tee').get(pk=pk)

    context = {
        'curr_time': curr_time(),
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)

def hole_index(request):
    courses = Course.objects.prefetch_related('hole').all()

    context = {
        'curr_time': curr_time(),
        'courses': courses,
    }

    return render(request, 'courses/hole_index.html', context)

def hole_detail(request, pk):
    hole = Hole.objects.prefetch_related('tee', 'green', 'fairway',
        'rough').get(pk=pk)

    context = {
        'curr_time': curr_time(),
        'hole': hole,
    }

    return render(request, 'courses/hole_detail.html', context)

def tee_index(request):
    tees = Tee.objects.all()

    context = {
        'curr_time': curr_time(),
        'tees': tees,
    }

    return render(request, 'courses/tee_index.html', context)

def tee_detail(request, pk):
    tee = Tee.objects.get(pk=pk)

    context = {
        'curr_time': curr_time(),
        'tee': tee,
    }

    return render(request, 'courses/tee_detail.html', context)

def tee_update(request, pk):

    return redirect('tee_detail', pk)

def fairway_index(request):
    fairways = Fairway.objects.all()

    context = {
        'curr_time': curr_time(),
        'fairways': fairways,
    }

    return render(request, 'courses/fairway_index.html', context)

def fairway_detail(request, pk):
    fairway = Fairway.objects.get(pk=pk)

    context = {
        'curr_time': curr_time(),
        'fairway': fairway,
    }

    return render(request, 'courses/fairway_detail.html', context)

def fairway_update(request, pk):

    return redirect('fairway_detail', pk)

def green_index(request):
    greens = Green.objects.all()

    context = {
        'curr_time': curr_time(),
        'greens': greens,
    }

    return render(request, 'courses/green_index.html', context)

def green_detail(request, pk):
    green = Green.objects.get(pk=pk)

    context = {
        'curr_time': curr_time(),
        'green': green,
    }

    return render(request, 'courses/green_detail.html', context)

def green_update(request, pk):

    return redirect('green_detail', pk)

def rough_index(request):
    roughs = Rough.objects.all()

    context = {
        'curr_time': curr_time(),
        'roughs': roughs,
    }

    return render(request, 'courses/rough_index.html', context)

def rough_detail(request, pk):
    rough = Rough.objects.get(pk=pk)

    context = {
        'curr_time': curr_time(),
        'rough': rough,
    }

    return render(request, 'courses/rough_detail.html', context)

def rough_update(request, pk):

    return redirect('rough_detail', pk)

def bunker_index(request):
    bunkers = Bunker.objects.all()

    context = {
        'curr_time': curr_time(),
        'bunkers': bunkers,
    }

    return render(request, 'courses/bunker_index.html', context)

def bunker_detail(request, pk):
    bunker = Bunker.objects.get(pk=pk)

    context = {
        'curr_time': curr_time(),
        'bunker': bunker,
    }

    return render(request, 'courses/bunker_detail.html', context)

def bunker_update(request, pk):

    return redirect('bunker_detail', pk) 
