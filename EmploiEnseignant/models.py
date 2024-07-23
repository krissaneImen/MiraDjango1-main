# models.py
from mongoengine import Document, StringField, FileField

class EmploiEnseignant(Document):
    anneeUniversitaire = StringField(required=True)
    semestre = StringField(required=True)
    NomEnseignant = StringField(required=True)
    CinEnseignant = StringField(required=True)
    type = StringField(required=True)
    emploiFile = FileField(required = False)  # Use FileField instead of StringField for file uploads
