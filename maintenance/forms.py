from django import forms

from .models import (
    OilChange,
    Repair,
    RepairPart
)

class RepairPartForm(forms.ModelForm):
    class Meta:
        model = RepairPart
        exclude = [
            'repair',
            'qty',
        ]

class OilChangeForm(forms.ModelForm):
    class Meta:
        model = OilChange
        exclude = [
            'oil_cost',
            'parts_cost',
            'total_cost',
            'updated_at',
        ]
        
class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        exclude = [
            'parts_cost',
            'total_cost',
            'updated_at',
        ]
