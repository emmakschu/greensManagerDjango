from django.contrib import admin

# Register your models here.

from .models import (
    Course, 
    Hole, 
    Tee, 
    Fairway, 
    Green, 
    Rough, 
    BunkerLocation, 
    Bunker
)

admin.site.register(Course)
admin.site.register(Hole)
admin.site.register(Tee)
admin.site.register(Fairway)
admin.site.register(Green)
admin.site.register(Rough)
admin.site.register(BunkerLocation)
admin.site.register(Bunker)
