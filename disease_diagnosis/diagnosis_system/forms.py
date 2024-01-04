from django import forms
from .models import Patient


class SymptomChoicesForm(forms.Form):
    symptoms = forms.CharField(max_length=250)


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'disease', 
            'symptom1', 
            'symptom2',
            'symptom3',
            'symptom4'
        ]
