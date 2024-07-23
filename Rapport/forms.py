# forms.py
from django import forms

class RapportForm(forms.Form):
    Cin = forms.CharField(max_length=500)
    anneeUniversitaire = forms.CharField(max_length=500)
    Titre = forms.CharField(max_length=500)
    NatureStage = forms.CharField(max_length=500)
    Version = forms.CharField(max_length=500)
    NomRaporteur = forms.CharField(max_length=200)
    CinRaporteur = forms.CharField(max_length=500)
    NomEtudiant = forms.CharField(max_length=200)
    Rapport = forms.FileField()
    