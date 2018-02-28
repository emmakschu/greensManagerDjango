from django.contrib import admin

# Register your models here.

from .models import (
    GreensMowing,
    TeeMowing,
    FairwayMowing,
    RoughMowing
)

admin.site.register(GreensMowing)
admin.site.register(TeeMowing)
admin.site.register(FairwayMowing)
admin.site.register(RoughMowing)
