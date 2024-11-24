from django import forms
from .models import Policy

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['policy_number', 'provider', 'policy_type', 'start_date', 'expiry_date', 'reminder_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'reminder_date': forms.DateInput(attrs={'type': 'date'}),
        }
