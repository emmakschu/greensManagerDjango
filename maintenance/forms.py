from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import (
    OilChange,
    Repair,
    RepairPart,
)

class OilChangeForm(forms.ModelForm):
    class Meta:
        model = OilChange
        exclude = [
            'oil_cost',
            'parts_used',
            'parts_cost',
            'total_cost',
            'updated_at',
        ]
        widgets = {
            'date_fixed': AdminDateWidget,
        }
        
class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        exclude = [
            'parts_used',
            'parts_cost',
            'total_cost',
            'updated_at',
            'created_at',
        ]

class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = Repair
        exclude = [
            'date_fixed',
            'parts_used',
            'parts_cost',
            'shipping_cost',
            'total_cost',
            'created_at',
            'updated_at'
        ]

class RepairPartForm(forms.ModelForm):
    class Meta:
        model = RepairPart
        exclude = [
            'repair'
        ]
