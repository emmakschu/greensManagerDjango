from django.shortcuts import render
from django.utils.timezone import now

from courses import models as Courses
from fertilizing import models as Fert
from irrigation import models as Irrig
from machines import models as Machines
from parts import models as Parts
from turfs import models as Turfs
from mowing import models as Mow
from rolling import models as Roll

def index(request):
    curr_time = now()
    course_list = Courses.Course.objects.all()
    hole_list = Courses.Hole.objects.all()
    box_probs = Irrig.SatelliteBox.objects.filter(problem=True)
    sprinkler_probs = \
        Irrig.SprinklerHead.objects.filter(problem=True)
    drain_probs = \
        Irrig.Drain.objects.filter(problem=True)
    oos_parts = \
        Parts.Part.objects.filter(in_stock=0) \
            .order_by('-updated_at')[:5]
    greens_mowing = \
        Mow.GreensMowing.objects.all().order_by('-mow_date')[:5]
    tee_mowing = \
        Mow.TeeMowing.objects.all().order_by('-mow_date')[:5]
    greens_rolling = \
        Roll.GreensRolling.objects.all().order_by('-roll_date')[:5]
    recent_fert = \
        Fert.Fertilizing.objects.all().order_by('-fert_date')[:5]
    greens_fert = \
        Fert.GreensFert.objects.all().order_by('-fert_date')[:5]
    tees_fert = \
        Fert.TeeFert.objects.all().order_by('-fert_date')[:5]
    ooc_machines = \
        Machines.Machine.objects.filter(in_commission=False) \
            .order_by('-updated_at')[:5]
    daily_notes = "/static/notes/%s" % (curr_time.strftime('%Y-%m-%d'))
    test_text = "Hello"

    context = {
        'curr_time': curr_time,
        'course_list': course_list,
        'hole_list': hole_list,
        'box_probs': box_probs,
        'sprinkler_probs': sprinkler_probs,
        'drain_probs': drain_probs,
        'oos_parts': oos_parts,
        'greens_mowing': greens_mowing,
        'tee_mowing': tee_mowing,
        'greens_roll': greens_rolling,
        'recent_fert': recent_fert,
        'greens_fert': greens_fert,
        'tees_fert': tees_fert,
        'ooc_machines': ooc_machines,
        'daily_notes': daily_notes,
        'test_text': test_text,
    }

    return render(request, 'welcome/index.html', context)

def daily(request):
    curr_time = now()

    context = {
        'curr_time': curr_time,
    }
    return render(request, 'welcome/daily.html', context)
