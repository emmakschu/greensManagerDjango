from django import forms

from .models import (
    Fertilizer,
    Fertilizing,
    GreensFert,
    TeeFert,
    FairwayFert,
    RoughFert
)

class FertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        exclude = [
            'created_at',
            'updated_at',
            'unit_price',
        ]
        
class GreensFertForm(forms.ModelForm):
    class Meta:
        model = GreensFert
        exclude = [
            'created_at',
            'updated_at',
            'cost'
        ]
        
class TeeFertForm(forms.ModelForm):
    class Meta:
        model = TeeFert
        exclude = [
            'created_at',
            'updated_at',
            'cost'
        ]

class FairwayFertForm(forms.ModelForm):
    class Meta:
        model = FairwayFert
        exclude = [
            'created_at',
            'updated_at',
            'cost'
        ]

class RoughFertForm(forms.ModelForm):
    class Meta:
        model = RoughFert
        exclude = [
            'created_at',
            'updated_at',
            'cost'
        ]
