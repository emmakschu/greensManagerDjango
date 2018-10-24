from django import forms

from .models import (
    SatelliteBox,
    SprinklerHead,
    QuickCoupler,
    Drain,
    ShutoffValve,
    IrrigationDig
)

import courses.models as Course

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

class IsoSearchForm(forms.Form):
    open = forms.BooleanField(required=False)
    latitude = forms.FloatField(required=False)
    longitude = forms.FloatField(required=False)
    tee = forms.ModelChoiceField(queryset=Course.Tee.objects.all(),
            required=False)
    green = forms.ModelChoiceField(queryset=Course.Green.objects.all(),
            required=False)
    fairway = forms.ModelChoiceField(queryset=Course.Fairway.objects.all(),
            required=False)
    rough = forms.ModelChoiceField(queryset=Course.Rough.objects.all(),
            required=False)
    problem = forms.BooleanField(required=False)
    handle = forms.CharField(required=False)

class IrrigationDigForm(forms.ModelForm):
    class Meta:
        model = IrrigationDig
        exclude = [
            'created_at',
            'updated_at'
        ]

class SprinklerSearchForm(forms.Form):
    latitude = forms.FloatField(required=False)
    longitude = forms.FloatField(required=False)
    box = forms.IntegerField(required=False)
    station = forms.IntegerField(required=False)

class QCSearchForm(forms.Form):
    latitude = forms.FloatField(required=False)
    longitude = forms.FloatField(required=False)

class ValveSearchForm(forms.Form):
    latitude = forms.FloatField(required=False)
    longitude = forms.FloatField(required=False)
    area = forms.CharField(required=False)
