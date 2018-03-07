from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)	
	created_by = models.ForeignKey(User, related_name="creator")
	updated_by = models.ForeignKey(User, related_name="editor")

	content = models.TextField()

class DailyNote(Note):
	valid_date = models.DateField()

class WeeklyNote(Note):
	start_date = models.DateField()
	end_date = models.DateField()
