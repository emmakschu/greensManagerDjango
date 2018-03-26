from django import forms

from .models import (
    Machine,
    Mower,
    GreensMower,
    TeeMower,
    FairwayMower,
    RoughMower,
    Roller,
    Aerator,
    Sprayer,
    Cart,
    TrapRake,
    UtilVehicle,
    Tractor,
    FertSpreader
)

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        exclude = [
            'created_at',
            'updated_at'
        ]

class MowerForm(forms.ModelForm):
    class Meta:
        model = Mower
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class GreensMowerForm(forms.ModelForm):
    class Meta:
        model = GreensMower
        exclude = [
            'created_at',
            'updated_at'
        ]

class TeeMowerForm(forms.ModelForm):
    class Meta:
        model = TeeMower
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class FairwayMowerForm(forms.ModelForm):
    class Meta:
        model = FairwayMower
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class RoughMowerForm(forms.ModelForm):
    class Meta:
        model = RoughMower
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class RollerForm(forms.ModelForm):
    class Meta:
        model = Roller
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class AeratorForm(forms.ModelForm):
    class Meta:
        model = Aerator
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class SprayerForm(forms.ModelForm):
    class Meta:
        model = Sprayer
        exclude = [
            'created_at',
            'updated_at'
        ]

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class TrapRakeForm(forms.ModelForm):
    class Meta:
        model = TrapRake
        exclude = [
            'created_at',
            'updated_at'
        ]

class UtilVehicleForm(forms.ModelForm):
    class Meta:
        model = UtilVehicle
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class TractorForm(forms.ModelForm):
    class Meta:
        model = Tractor
        exclude = [
            'created_at',
            'updated_at'
        ]
        
class FertSpreaderForm(forms.ModelForm):
    class Meta:
        model = FertSpreader
        exclude = [
            'created_at',
            'updated_at'
        ]
