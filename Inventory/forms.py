from django import forms
from Inventory.models import trucks, smallVehicles


class trucksForms(forms.ModelForm):
    class Meta:
        model = trucks
        fields = "__all__"
        widgets = {
            'registration': forms.DateInput(attrs={'placeholder': 'Select Date', 'type': 'date'}),
            'inspection': forms.DateInput(attrs={'placeholder': 'Select Date', 'type': 'date'}),
        }


class smallVehiclesForm(forms.ModelForm):
    class Meta:
        model = smallVehicles
        fields = "__all__"
        widgets = {
            'registration': forms.DateInput(attrs={'placeholder': 'Select Date', 'type': 'date'}),
            'inspection': forms.DateInput(attrs={'placeholder': 'Select Date', 'type': 'date'}),
        }

