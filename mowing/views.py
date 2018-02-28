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
    greens_mow = \
        Mow.GreensMowing.objects.all().order_by('-mow_date')[:5]
    last_greens = curr_time - greens_mow.first().mow_date
    last_greens = "%d days, %02d:%02d" % (
        last_greens.days,
        last_greens.seconds / 3600,
        (last_greens.seconds / 60) % 60
    )

    tee_mow = \
        Mow.TeeMowing.objects.all().order_by('-mow_date')[:5]
    last_tees = curr_time - tee_mow.first().mow_date
    last_tees = "%d days, %02d:%02d" % (
        last_tees.days,
        last_tees.seconds / 3600,
        (last_tees.seconds / 60) % 60
    )

    fairway_mow = \
        Mow.FairwayMowing.objects.all().order_by('-mow_date')[:5]
    last_fairway = curr_time - fairway_mow.first().mow_date
    last_fairway = "%d days, %02d:%02d" % (
        last_fairway.days,
        last_fairway.seconds / 3600,
        (last_fairway.seconds / 60) % 60
    )

    rough_mow = \
        Mow.RoughMowing.objects.all().order_by('-mow_date')[:5]
    last_rough = curr_time - rough_mow.first().mow_date
    last_rough = "%d days, %02d:%02d" % (
        last_rough.days,
        last_rough.seconds / 3600,
        (last_rough.seconds / 60) % 60
    )

    context = {
        'curr_time': curr_time,
        'greens_mow': greens_mow,
        'last_greens': last_greens,
        'tee_mow': tee_mow,
        'last_tees': last_tees,
        'fairway_mow': fairway_mow,
        'last_fairway': last_fairway,
        'rough_mow': rough_mow,
        'last_rough': last_rough
    }

    return render(request, 'mowing/index.html', context)