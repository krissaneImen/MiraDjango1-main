# models.py
from mongoengine import Document, StringField, FileField,ListField ,DateTimeField


class EvaluationJournale(Document):
    idJournale = StringField(required=True)
    Cin = StringField(required=True)
    NomRapporteur = StringField(required=True)
    FormeExpression = StringField(required=True)
    FormePesentation = StringField(required=True)
    PresentationEntreprise  = StringField(required=True)
    ValeurScien = StringField(required=True)
    EffortPersonnel = StringField(required=True)
    Documentation = StringField(required=True)
    ContactEntreprise = StringField(required=True)
    Observation = StringField(required=True)