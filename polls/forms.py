from django import forms
from . import models

class accountForm(forms.ModelForm):
    class Meta:
        model = models.account
        fields = '__all__'