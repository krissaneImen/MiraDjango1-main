# forms.py
from django import forms

class CalandrierForm(forms.Form):
    Nom = forms.CharField(max_length=200)
    semestre = forms.CharField(max_length=200)
    AU = forms.CharField(max_length=200)
    fichier = forms.FileField()
    