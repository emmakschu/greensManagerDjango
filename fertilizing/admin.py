from django.contrib import admin

# Register your models here.

from .models import (
    Fertilizer,
    GreensFert,
    TeeFert,
    FairwayFert,
    RoughFert
)

admin.site.register(Fertilizer)
admin.site.register(GreensFert)
admin.site.register(TeeFert)
admin.site.register(FairwayFert)
admin.site.register(RoughFert)
