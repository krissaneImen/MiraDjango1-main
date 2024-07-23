from mongoengine import Document, StringField , FileField, BooleanField
from django.utils import timezone

class Reglement(Document):
    identifiant = StringField( unique=True)
    name = StringField(default='')
    description = StringField(default='')
    type = StringField(max_length=150, null=False)
    etudiant = BooleanField(default=False)
    enseignant = BooleanField(default=False)
    administratif = BooleanField(default=False)
    administrateur = BooleanField(default=False)

