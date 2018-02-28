from django.contrib import admin

# Register your models here.

from .models import (
    GreensRolling,
    TeeRolling,
    FairwayRolling
)

admin.site.register(GreensRolling)
admin.site.register(TeeRolling)
admin.site.register(FairwayRolling)
