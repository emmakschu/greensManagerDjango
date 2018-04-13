from django.contrib import admin

from .models import (
    SandType,
    GreenTopdressing,
    TeeTopdressing,
    FairwayTopdressing,
)

admin.site.register(SandType)
admin.site.register(GreenTopdressing)
admin.site.register(TeeTopdressing)
admin.site.register(FairwayTopdressing)
