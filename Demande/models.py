from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField, EmailField
from django.utils import timezone

class Demande(Document):
    Demande = StringField(max_length=1000, verbose_name='Demande')
    Responsable = StringField(max_length=150, verbose_name='Demande')
    Cin = StringField(max_length=150, verbose_name='Cin')
    DateDemande= DateTimeField(default=timezone.now)
    PretLe = DateTimeField(default=timezone.now)
    Etat = StringField(max_length=150, verbose_name='Etat')
    
