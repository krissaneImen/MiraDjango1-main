from rest_framework import serializers
from .models import EvaluationJournale

class EvaluationJournaleJournale(serializers.Serializer):
    idJournale = serializers.CharField(max_length=200)
    Cin = serializers.CharField(max_length=200)
    NomRapporteur = serializers.CharField(max_length=500)
    FormeExpression = serializers.CharField(max_length=500)
    FormePesentation = serializers.CharField(max_length=500)
    PresentationEntreprise = serializers.CharField(max_length=1000)
    ValeurScien = serializers.CharField(max_length=1000)
    EffortPersonnel = serializers.CharField(max_length=1000)
    Documentation = serializers.CharField(max_length=1000)
    ContactEntreprise = serializers.CharField(max_length=1000)
    Observation = serializers.CharField(max_length=1000)
    
    def create(self, validated_data):
        return EvaluationJournale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.NomRapporteur = validated_data.get('NomRapporteur', instance.NomRapporteur)
        instance.FormeExpression = validated_data.get('FormeExpression', instance.FormeExpression)
        instance.FormePesentation = validated_data.get('FormePesentation', instance.FormePesentation)
        instance.PresentationEntreprise = validated_data.get('PresentationEntreprise', instance.PresentationEntreprise)
        instance.ValeurScien = validated_data.get('ValeurScien', instance.ValeurScien)
        instance.EffortPersonnel = validated_data.get('EffortPersonnel', instance.EffortPersonnel)
        instance.Documentation = validated_data.get('Documentation', instance.Documentation)
        instance.ContactEntreprise = validated_data.get('ContactEntreprise', instance.ContactEntreprise)
        instance.Observation = validated_data.get('Observation', instance.Observation)
        instance.save()
        return instance
