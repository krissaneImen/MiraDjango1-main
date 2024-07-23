from django.utils import timezone
from mongoengine import Document, StringField, ListField ,DateField


class Avis(Document):
    type = StringField(max_length=500, verbose_name='type')
    etat = StringField(max_length=500, verbose_name='etat')
    enseignant = StringField(max_length=500, verbose_name='etat')
    cinEnseignant = StringField(max_length=500, verbose_name='etat')
    heureDebut = StringField(max_length=500, verbose_name='etat')
    heureFin = StringField(max_length=500, verbose_name='etat')
    DateAvis = DateField( default=timezone.now, null=True, verbose_name='Date d\'avis')
    Datefin = DateField( default=timezone.now, null=True, verbose_name='Date Fin')
    Anneeuniversitaire = StringField(max_length=100, verbose_name='Lieu de Formation')
    Classes = ListField(StringField(max_length=200), verbose_name='Membres')