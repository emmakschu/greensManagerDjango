from django.contrib import admin

from .models import (
	DailyNote,
	WeeklyNote
)

admin.site.register(DailyNote)
admin.site.register(WeeklyNote)