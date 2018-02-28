from django.shortcuts import render
from django.utils.timezone import now

from courses.models import (
    Course,
    Hole,
    Tee,
    Green,
    Fairway,
    Bunker
)

def index(request):
    curr_time = now()
    courses = Course.objects.all()
    holes = Hole.objects.all()

    context = {
        'curr_time': curr_time,
        'courses': courses,
        'holes': holes,
    }
    return render(request, 'courses/index.html', context)
