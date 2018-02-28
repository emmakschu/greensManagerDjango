from django.contrib import admin

# Register your models here.

from .models import (
    SatelliteBox,
    SprinklerHead,
    QuickCoupler,
    Drain,
    IrrigationDig
)

admin.site.register(SatelliteBox)
admin.site.register(SprinklerHead)
admin.site.register(QuickCoupler)
admin.site.register(Drain)
admin.site.register(IrrigationDig)

