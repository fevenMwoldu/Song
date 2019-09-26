from django import forms
from .models import Mezmur

'''
   Form for the Mezmur model
'''
class MezmurForm(forms.ModelForm):
    class Meta:
        model = Mezmur
        exclude = []
