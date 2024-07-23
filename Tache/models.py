# models.py
from mongoengine import Document, StringField,DateTimeField ,DateField
from django.utils import timezone

class Tache(Document):
    idJournale = StringField(required=True)
    TacheJournaliere = StringField(required=True)
    Date = DateField( null=True, verbose_name='Date')
    LastModified = DateField( null=True, verbose_name='LastModified')
    