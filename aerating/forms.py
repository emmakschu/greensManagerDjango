from django import forms

from .models import (
    Aerating,
    GreensAerating,
    TeeAerating,
    FairwayAerating,
    RoughAerating,
    QuadraTining,
    DeepTine,
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
    
class QuadraTiningForm(forms.ModelForm):
    class Meta:
        model = QuadraTining
        exclude = [
            'created_at',
            'updated_at',
        ]

class DeepTineForm(forms.ModelForm):
    class Meta:
        model = DeepTine
        exclude = [
            'created_at',
            'updated_at',
        ]
