from django import forms

from .models import (
    BuildGreen,
    BuildTee,
    BuildFairway,
    BuildBunker,
)

class BuildGreenForm(forms.ModelForm):
    class Meta:
        model = BuildGreen
        exclude = [
            'created_at',
            'updated_at',
        ]
        
class BuildTeeForm(forms.ModelForm):
    class Meta:
        model = BuildTee
        exclude = [
            'created_at',
            'updated_at',
        ]
        
class BuildFairwayForm(forms.ModelForm):
    class Meta:
        model = BuildFairway
        exclude = [
            'created_at',
            'updated_at',
        ]
        
class BuildBunkerForm(forms.ModelForm):
    class Meta:
        model = BuildBunker
        exclude = [
            'created_at',
            'updated_at',
        ]
