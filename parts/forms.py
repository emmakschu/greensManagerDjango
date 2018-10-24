from django import forms


from .models import (
    Fluid,
    Fuel,
    Oil,
    Part,
    Filter
)

class FuelForm(forms.ModelForm):
    class Meta:
        model = Fuel
        exclude = [
            'created_at',
            'updated_at',
            'price_per_unit',
        ]
        
class OilForm(forms.ModelForm):
    class Meta:
        model = Oil 
        exclude = [
            'created_at',
            'updated_at',
            'price_per_unit',
        ]

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        exclude = [
            'created_at',
            'updated_at',
        ]
        
class FilterForm(forms.ModelForm):
    class Meta:
        model = Filter
        exclude = [
            'created_at',
            'updated_at',
        ]

class PartsSearchForm(forms.Form):
    part_no = forms.CharField(required=False)
    make = forms.CharField(required=False)
    description = forms.CharField(required=False)
    location = forms.CharField(required=False)
