from django import forms

from .models import (
    Aerating,
    GreensAerating,
    TeeAerating,
    FairwayAerating,
    RoughAerating
)

class AeratingForm(forms.ModelForm):
    class Meta:
        model = Aerating
        exclude = [
            'created_at',
            'updated_at',
        ]
        
class GreensAeratingForm(forms.ModelForm):
    class Meta:
        model = GreensAerating
        exclude = [
            'created_at',
            'updated_at',
        ]
        
class TeeAeratingForm(forms.ModelForm):
    class Meta:
        model = TeeAerating
        exclude = [
            'created_at',
            'updated_at',
        ]

class FairwayAeratingForm(forms.ModelForm):
    class Meta:
        model = FairwayAerating
        exclude = [
            'created_at',
            'updated_at',
        ]
                        
class RoughAeratingForm(forms.ModelForm):
    class Meta:
        model = RoughAerating
        exclude = [
            'created_at',
            'updated_at',
        ]
    
