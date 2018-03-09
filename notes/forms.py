from django import forms

from .models import DailyNote, WeeklyNote 

class DailyNoteEdit(forms.ModelForm):
	class Meta:
		model = DailyNote 
		exclude = [
			'created_by',
			'updated_by',
			'valid_date'
		]

class WeeklyNoteEdit(forms.ModelForm):
	class Meta:
		model = WeeklyNote
		exclude = [
			'created_by',
			'updated_by',
			'start_date'
		]