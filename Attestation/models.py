from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField, EmailField
from django.utils import timezone

class Attestation(Document):
    Nom = StringField(max_length=1000, verbose_name='Nom')
    type = StringField(max_length=1000, verbose_name='type')
    idDemande = StringField(max_length=1000, verbose_name='Nom')
    Cin = StringField(max_length=150, verbose_name='Cin')
    Etat = StringField(max_length=150, verbose_name='Etat')
    
