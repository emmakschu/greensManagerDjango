from django.contrib import admin

# Register your models here.

from .models import (
    GreensMower,
    TeeMower,
    FairwayMower,
    RoughMower,
    Roller,
    Aerator,
    Sprayer,
    Cart,
    TrapRake,
    UtilVehicle,
    Tractor,
    FertSpreader,
    Truck,
    HourReading,
)

admin.site.register(GreensMower)
admin.site.register(TeeMower)
admin.site.register(FairwayMower)
admin.site.register(RoughMower)
admin.site.register(Roller)
admin.site.register(Aerator)
admin.site.register(Sprayer)
admin.site.register(Cart)
admin.site.register(TrapRake)
admin.site.register(UtilVehicle)
admin.site.register(Tractor)
admin.site.register(FertSpreader)
admin.site.register(Truck)
admin.site.register(HourReading)
