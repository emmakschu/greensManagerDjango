from django import forms

from .models import (
    SatelliteBox,
    SprinklerHead,
    QuickCoupler,
    Drain,
    ShutoffValve,
    IrrigationDig
)

class SatelliteBoxForm(forms.ModelForm):
    class Meta:
        model = SatelliteBox
        exclude = [
            'created_at',
            'updated_at'
        ]

class SprinklerHeadForm(forms.ModelForm):
    class Meta:
        model = SprinklerHead
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class QuickCouplerForm(forms.ModelForm):
    class Meta:
        model = QuickCoupler
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class DrainForm(forms.ModelForm):
    class Meta:
        model = Drain
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class ShutoffValveForm(forms.ModelForm):
    class Meta:
        model = ShutoffValve
        exclude = [
            'created_at',
            'updated_at'
        ]

class IrrigationDigForm(forms.ModelForm):
    class Meta:
        model = IrrigationDig
        exclude = [
            'created_at',
            'updated_at'
        ]
