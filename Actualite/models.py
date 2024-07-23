from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField, EmailField, ListField , FileField
from django.utils import timezone

class Actualite(Document):
    anneeUniversitaire = StringField(default='')
    date = DateTimeField(default=timezone.now)
    intitule = StringField(max_length=150, null=False)
    etudiant = BooleanField(default=False)
    enseignant = BooleanField(default=False)
    administratif = BooleanField(default=False)
    administrateur = BooleanField(default=False)
    fichier = FileField(required=False)  # Use FileField instead of StringField for file uploads


