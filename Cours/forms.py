# forms.py
from django import forms

class SupportForm(forms.Form):
    Titre = forms.CharField(max_length=500)
    DateAjout = forms.DateField( )
    Description = forms.CharField(max_length=1500)
    Support = forms.FileField()
    