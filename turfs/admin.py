from django.contrib import admin

# Register your models here.

from .models import (
    SoilType,
    TurfgrassGenus,
    TurfgrassSpecies,
    Cultivar
)

admin.site.register(SoilType)
admin.site.register(TurfgrassGenus)
admin.site.register(TurfgrassSpecies)
admin.site.register(Cultivar)
