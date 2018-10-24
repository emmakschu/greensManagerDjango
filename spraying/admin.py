from django.contrib import admin

from .models import (
    Pest,
    ChemManufacturer,
    Chemical,
    TradeChem,
    Spraying,
    ChemUsedInSpray,
    GreensSpraying,
    TeeSpraying,
    FairwaySpraying,
    RoughSpraying
)

admin.site.register(Pest)
admin.site.register(ChemManufacturer)
admin.site.register(Chemical)
admin.site.register(TradeChem)
admin.site.register(Spraying)
admin.site.register(ChemUsedInSpray)
admin.site.register(GreensSpraying)
admin.site.register(TeeSpraying)
admin.site.register(FairwaySpraying)
admin.site.register(RoughSpraying)
