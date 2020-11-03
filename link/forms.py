from django import forms

from .models import Specification


class SpecificationCreateForm(forms.ModelForm):
    class Meta:
        model = Specification
        exclude = ['created_at']
