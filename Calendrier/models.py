# models.py
from mongoengine import Document, StringField, FileField ,IntField

class Calandrier(Document):
    Nom = StringField(required=True)
    AU = StringField(required=True)
    semestre = StringField(required=True)
    fichier = FileField(required=True)  # Use FileField instead of StringField for file uploads
