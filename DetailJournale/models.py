# models.py
from mongoengine import Document, StringField,BooleanField, FileField,ListField ,DateTimeField


class DetailJournale(Document):
    anneeUniversitaire = StringField(required=True)
    Nom = StringField(required=True)
    Cin = StringField(required=True)
    Prenom = StringField(required=True)
    Departement = StringField(required=True)
    Option = StringField(required=True)
    Entreprise = StringField(required=True)
    Adress = StringField(required=True)
    Fax = StringField(required=True)
    NatureStage = StringField(required=True)
    PeriodeStage = StringField(required=True)
    etatEvaluation = StringField(default='Évaluation en attente',  verbose_name='etatEvaluation')
   