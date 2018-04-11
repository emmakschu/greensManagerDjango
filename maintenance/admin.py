from django.contrib import admin

from .models import (
    Maintenance,
    OilChange,
    Repair,
    RepairPart
)

admin.site.register(Maintenance)
admin.site.register(OilChange)
admin.site.register(Repair)
admin.site.register(RepairPart)
