from django.shortcuts import render
from django.utils.timezone import now

from . import models as Mach
from maintenance import models as Maint

def index(request):
    curr_time = now()

    context = {
        'curr_time': curr_time,
    }

    return render(request, 'machines/index.html', context)

def mower(request, mower_id):
    curr_time = now()

    mower = Mach.GreensMower.objects.get(pk=mower_id)
    oil_changes = Maint.OilChange.objects.filter(machine=mower)[:5]

    context = {
        'curr_time': curr_time,
        'mower': mower,
        'oil_changes': oil_changes,
    }

    return render(request, 'machines/mower.html', context)
