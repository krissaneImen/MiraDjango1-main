from rest_framework import serializers
from .models import EvaluationStage

class EvaluationStageSerializer(serializers.Serializer):
    idStage = serializers.CharField(max_length=200)
    DateEvaluation = serializers.CharField(max_length=200)
    CinEtudiant = serializers.CharField(max_length=500)
    NomEtudiant = serializers.CharField(max_length=500)
    Groupe = serializers.CharField(max_length=500)
    SocieteAccueil = serializers.CharField(max_length=1000)
    CinPresident = serializers.CharField(max_length=1000)
    President = serializers.CharField(max_length=1000)
    Rapporteur = serializers.CharField(max_length=1000)
    CinRapporteur = serializers.CharField(max_length=1000)
    Rapport = serializers.CharField(max_length=1000)
    FondRapport = serializers.CharField(max_length=1000)
    formeRapport = serializers.CharField(max_length=1000)
    JournaleStage = serializers.CharField(max_length=1000)
    QualiteJournale = serializers.CharField(max_length=1000)
    QualitePresentation = serializers.CharField(max_length=1000)
    RemarqueEncadrantPro = serializers.CharField(max_length=1000)
    Presentation = serializers.CharField(max_length=1000)
    QualiteSpeech = serializers.CharField(max_length=1000)
    ReactionQuestion = serializers.CharField(max_length=1000)
    clarteExpression = serializers.CharField(max_length=1000)
    CapaciteConvaincre = serializers.CharField(max_length=1000)
    ValiditeStage = serializers.CharField(max_length=1000)
    NoteFinale = serializers.CharField(max_length=1000)
    Observation = serializers.CharField(max_length=1000)
    
    def create(self, validated_data):
        return EvaluationStage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.DateEvaluation = validated_data.get('DateEvaluation', instance.DateEvaluation)
        instance.CinEtudiant = validated_data.get('CinEtudiant', instance.CinEtudiant)
        instance.NomEtudiant = validated_data.get('NomEtudiant', instance.NomEtudiant)
        instance.Groupe = validated_data.get('Groupe', instance.Groupe)
        instance.SocieteAccueil = validated_data.get('SocieteAccueil', instance.SocieteAccueil)
        instance.CinPresident = validated_data.get('CinPresident', instance.CinPresident)
        instance.President = validated_data.get('President', instance.President)
        instance.Rapporteur = validated_data.get('Rapporteur', instance.Rapporteur)
        instance.CinRapporteur = validated_data.get('CinRapporteur', instance.CinRapporteur)
        instance.Rapport = validated_data.get('Rapport', instance.Rapport)
        instance.FondRapport = validated_data.get('FondRapport', instance.FondRapport)
        instance.formeRapport = validated_data.get('formeRapport', instance.formeRapport)
        instance.JournaleStage = validated_data.get('JournaleStage', instance.JournaleStage)
        instance.QualiteJournale = validated_data.get('QualiteJournale', instance.QualiteJournale)
        instance.RemarqueEncadrantPro = validated_data.get('RemarqueEncadrantPro', instance.RemarqueEncadrantPro)
        instance.Presentation = validated_data.get('Presentation', instance.Presentation)
        instance.QualitePresentation = validated_data.get('QualitePresentation', instance.QualitePresentation)
        instance.QualiteSpeech = validated_data.get('QualiteSpeech', instance.QualiteSpeech)
        instance.ReactionQuestion = validated_data.get('ReactionQuestion', instance.ReactionQuestion)
        instance.clarteExpression = validated_data.get('clarteExpression', instance.clarteExpression)
        instance.CapaciteConvaincre = validated_data.get('CapaciteConvaincre', instance.CapaciteConvaincre)
        instance.ValiditeStage = validated_data.get('ValiditeStage', instance.ValiditeStage)
        instance.NoteFinale = validated_data.get('NoteFinale', instance.NoteFinale)
        instance.Observation = validated_data.get('Observation', instance.Observation)
        instance.save()
        return instance