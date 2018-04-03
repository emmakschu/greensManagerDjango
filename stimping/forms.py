from django import forms

from .models import Stimp

class StimpForm(forms.ModelForm):
    class Meta:
        model = Stimp
        exclude = [
            'created_at',
            'updated_at',
            'forwardAvg',
            'backwardAvg',
            'leftAvg',
            'rightAvg',
            'stdDev',
            'mu_k',
            'raw_speed',
            'adj_speed'
        ]

class SimpleStimpForm(forms.ModelForm):
    class Meta:
        model = Stimp
        exclude = [
            'created_at',
            'updated_at',
            'forward2',
            'forward3',
            'forwardAvg',
            'backward2',
            'backward3',
            'backwardAvg',
            'left2',
            'left3',
            'leftAvg',
            'right2',
            'right3',
            'rightAvg',
            'stdDev',
            'mu_k',
            'raw_speed',
            'adj_speed'
        ]
