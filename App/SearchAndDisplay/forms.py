from django import forms

from .models import ExpertUser

class ExpertUserForm(forms.ModelForm):
    class Meta:
        model = ExpertUser