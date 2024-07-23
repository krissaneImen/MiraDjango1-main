# forms.py
from django import forms

class PhotocopieForm(forms.Form):
    cin = forms.CharField(max_length=100)
    idDemande = forms.CharField(max_length=100)
    nombreCopie = forms.CharField(max_length=100)
    NomEnseignant = forms.CharField(max_length=100)
    cour = forms.CharField(max_length=100)
    fichier = forms.FileField()
    