from django.contrib import admin

from .models import (
    GreensAerating,
    TeeAerating,
    FairwayAerating,
    RoughAerating,
    QuadraTining,
    DeepTine,
)

admin.site.register(GreensAerating)
admin.site.register(TeeAerating)
admin.site.register(FairwayAerating)
admin.site.register(RoughAerating)
admin.site.register(QuadraTining)
admin.site.register(DeepTine)
