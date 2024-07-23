# models.py
from mongoengine import Document, StringField, FileField ,BooleanField

class ReglementPdf(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    pdf_file = FileField(required=True)
    type = StringField(required=True)
    etudiant = BooleanField(default=False)
    enseignant = BooleanField(default=False)
    administratif = BooleanField(default=False)
    administrateur = BooleanField(default=False)