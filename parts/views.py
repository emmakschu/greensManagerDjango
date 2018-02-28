from django.shortcuts import render
from django.utils.timezone import now

from . import models as Part

def index(request):
    curr_time = now()
    recently_added = \
        Part.Part.objects.all().order_by('-created_at')[:10]
    recently_updated = \
        Part.Part.objects.all().order_by('-updated_at')[:10]
    oos = \
        Part.Part.objects.filter(in_stock=0).order_by('-updated_at')[:10]

    context = {
        'curr_time': curr_time,
        'recently_added': recently_added,
        'recently_updated': recently_updated,
        'oos': oos,
    }

    return render(request, 'parts/index.html', context)

def all(request):
    return render(request, 'parts/all.html')
