from django import forms

class TypeGlogableForm(forms.Form):
    name = forms.CharField(max_length=250, label='Nom')
    fonctionalite = forms.CharField(max_length=250, label='Fonctionnalité')
    etudiant = forms.BooleanField(label='Étudiant', required=False)
    enseignant = forms.BooleanField(label='Enseignant', required=False)
    administratif = forms.BooleanField(label='Administratif', required=False)
    administrateur = forms.BooleanField(label='Administrateur', required=False)
