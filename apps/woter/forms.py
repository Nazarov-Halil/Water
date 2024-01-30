from django import forms
from .models import Water


class WaterForm(forms.ModelForm):
    class Meta:
        model = Water
        fields = ['location', 'date', 'water_Liter', 'quantity']
