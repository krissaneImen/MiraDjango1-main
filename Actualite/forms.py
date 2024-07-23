from django import forms
from django.utils import timezone

class ActualiteForm(forms.Form):
    anneeUniversitaire = forms.CharField(max_length=100)
    intitule = forms.CharField(max_length=150)
    etudiant = forms.BooleanField(required=False)
    enseignant = forms.BooleanField(required=False)
    administratif = forms.BooleanField(required=False)
    administrateur = forms.BooleanField(required=False)
    date = forms.DateTimeField(initial=timezone.now)
    fichier = forms.FileField()
