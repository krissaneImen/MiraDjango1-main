# models.py
from mongoengine import Document, StringField, FileField ,IntField

class Photocopie(Document):
    cin = StringField(required=True)
    idDemande = StringField(required=True)
    nombreCopie = StringField(required=True)
    NomEnseignant = StringField(required=True)
    cour = StringField(required=True)
    fichier = FileField(required=True)  # Use FileField instead of StringField for file uploads
