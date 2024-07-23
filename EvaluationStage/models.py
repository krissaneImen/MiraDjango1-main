from mongoengine import Document, StringField, DateField
from django.utils import timezone

class EvaluationStage(Document):
    idStage = StringField(required=True)
    DateEvaluation = DateField( default=timezone.now, null=True, verbose_name='Date de Seance')
    CinEtudiant = StringField(required=True)
    NomEtudiant = StringField(required=True)
    Groupe = StringField(required=True)
    SocieteAccueil = StringField(required=True)
    CinPresident = StringField()
    President = StringField()
    Rapporteur  = StringField()
    CinRapporteur = StringField()
    Rapport = StringField(required=True)
    FondRapport = StringField(required=True)
    formeRapport = StringField(required=True)
    JournaleStage = StringField(required=True)
    QualiteJournale = StringField(required=True)
    RemarqueEncadrantPro = StringField(required=True)
    Presentation = StringField(required=True)
    QualitePresentation = StringField(required=True)
    QualiteSpeech = StringField(required=True)
    ReactionQuestion = StringField(required=True)
    clarteExpression = StringField(required=True)
    CapaciteConvaincre = StringField(required=True)
    ValiditeStage = StringField(required=True)
    NoteFinale = StringField(required=True)
    Observation = StringField(required=True)

    