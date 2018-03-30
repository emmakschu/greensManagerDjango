from django import forms

from .models import (
    GreensRolling,
    TeeRolling,
    FairwayRolling
)

class GreensRollingForm(forms.ModelForm):
    class Meta:
        model = GreensRolling
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class TeeRollingForm(forms.ModelForm):
    class Meta:
        model = TeeRolling
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class FairwayRollingForm(forms.ModelForm):
    class Meta:
        model = FairwayRolling
        exclude = [
            'created_at',
            'updated_at'
        ]
