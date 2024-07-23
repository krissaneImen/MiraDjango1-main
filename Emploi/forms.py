# forms.py
from django import forms

class UploadFileForm(forms.Form):
    anneeUniversitaire = forms.CharField(max_length=100)
    semestre = forms.CharField(max_length=100)
    classes = forms.CharField(max_length=100)
    type = forms.CharField(max_length=100)
    emploiFile = forms.FileField()
    