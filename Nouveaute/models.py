from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField, EmailField, ListField , FileField
from django.utils import timezone

class Nouveaute(Document):
    Identifiant = StringField(max_length=20, unique=True, required=True, verbose_name='Numéro de carte d\'identité nationale')
    anneeUniversitaire = StringField(default='')
    date = DateTimeField(default=timezone.now)
    intitule = StringField(max_length=150, null=False)
    etudiant = BooleanField(default=False)
    enseignant = BooleanField(default=False)
    administratif = BooleanField(default=False)
    administrateur = BooleanField(default=False)
    image = StringField(blank=True, default='')
