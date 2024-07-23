from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField, EmailField, ListField , FileField
from django.utils import timezone

class TypeGlogable(Document):
    name = StringField(default='')
    fonctionalite = StringField(max_length=150, null=False)
    etudiant = BooleanField(default=False)
    enseignant = BooleanField(default=False)
    administratif = BooleanField(default=False)
    administrateur = BooleanField(default=False)
    
