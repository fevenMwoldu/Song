from django import forms
from .models import Song

'''
   Form for the Mezmur model
'''
class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = []
