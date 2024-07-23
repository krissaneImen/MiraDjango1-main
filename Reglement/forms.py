# forms.py
from django import forms

class ReglementForm(forms.Form):
    name = forms.CharField(max_length=500)
    description = forms.CharField(max_length=600)
    pdf_file = forms.FileField()
    type = forms.CharField(max_length=200)
    etudiant = forms.BooleanField()
    enseignant = forms.BooleanField()
    administratif = forms.BooleanField()
    administrateur = forms.BooleanField()

    