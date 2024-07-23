# models.py
from mongoengine import Document, StringField, FileField , DateField 
from django.utils import timezone

class SupportCours(Document):
    Titre = StringField(required=True)
    DateAjout = DateField( default=timezone.now, null=True, verbose_name='Date de Seance')
    Description = StringField(required=False)
    Support = FileField(required=True)  
