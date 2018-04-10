from django.contrib import admin

from .models import (
    GreensAerating,
    TeeAerating,
    FairwayAerating,
    RoughAerating
)

admin.site.register(GreensAerating)
admin.site.register(TeeAerating)
admin.site.register(FairwayAerating)
admin.site.register(RoughAerating)
