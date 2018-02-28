from django.contrib import admin

# Register your models here.

from .models import (
    Fuel,
    Oil,
    Part,
    Filter
)

admin.site.register(Fuel)
admin.site.register(Oil)
admin.site.register(Part)
admin.site.register(Filter)
