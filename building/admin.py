from django.contrib import admin

from .models import (
    BuildGreen,
    BuildTee,
    BuildFairway,
    BuildBunker
)

admin.site.register(BuildGreen)
admin.site.register(BuildTee)
admin.site.register(BuildFairway)
admin.site.register(BuildBunker)
