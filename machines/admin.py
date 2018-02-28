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
    Tractor
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

