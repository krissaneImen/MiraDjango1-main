# models.py
from mongoengine import Document, StringField, FileField 

class Rapport(Document):
    Cin = StringField(required=True)
    anneeUniversitaire = StringField(required=True)
    NatureStage = StringField(required=True)
    Titre = StringField(required=True)
    Version = StringField(required=False)
    NomEtudiant = StringField(required=True)
    NomRaporteur = StringField(null=True, required=False ,default="Non attribué" )
    CinRaporteur = StringField(null=True, required=False)
    Rapport = FileField(required=True)  
