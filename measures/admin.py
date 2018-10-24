from django.contrib import admin

from .models import (
    Unit,
    WeightUnit,
    VolumeUnit,
    DistanceUnit,
    AreaUnit,
    TimeUnit,
    RateUnit
)

admin.site.register(Unit)
admin.site.register(WeightUnit)
admin.site.register(VolumeUnit)
admin.site.register(DistanceUnit)
admin.site.register(AreaUnit)
admin.site.register(TimeUnit)
admin.site.register(RateUnit)
