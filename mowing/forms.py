from django import forms

from .models import (
    GreensMowing,
    TeeMowing,
    FairwayMowing,
    RoughMowing,
)

"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

REMEMBER TO INCREMENT `mow_direction` OF TurfFeature INSTANCE WHEN APPLYING A
MOWING INSTANCE TO IT!!!!!!!!!


For greens

	mow_direction += pi / 4
	if mow_direction >= pi:
		mow_direction -= pi

For tees

	mow_direction += pi / 4
	if mow_direction == pi / 2:
		mow_direction += pi / 4
	if mow_direction >= pi:
		mow_direction -= pi

For fairways

	mow_direction += pi / 2
	if mow_direction >= pi:
		mow_direction -= pi

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

class GreensMowingForm(forms.ModelForm):
    class Meta:
        model = GreensMowing
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class TeeMowingForm(forms.ModelForm):
    class Meta:
        model = TeeMowing
        exclude = [
            'created_at',
            'updated_at',
        ]
        
class FairwayMowingForm(forms.ModelForm):
    class Meta:
        model = FairwayMowing
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class RoughMowingForm(forms.ModelForm):
    class Meta:
        model = RoughMowing
        exclude = [
            'created_at',
            'updated_at'
        ]
