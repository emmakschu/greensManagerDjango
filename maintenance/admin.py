from django.contrib import admin

from .models import (
    Maintenance,
    OilChange,
    Repair,
    RepairPart,
    BedknifeToReel,
)

admin.site.register(Maintenance)
admin.site.register(OilChange)
admin.site.register(Repair)
admin.site.register(RepairPart)
admin.site.register(BedknifeToReel)
