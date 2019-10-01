from django import forms
from .models import Plant
    
class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['plant_name', 'plant_hum', 'plant_temp', 'plant_hi', 'foto']