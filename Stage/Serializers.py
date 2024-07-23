from rest_framework import serializers
from .models import Stage

class StageSerializer(serializers.Serializer):
    anneeUniversitaire = serializers.CharField()
    Departement = serializers.CharField()
    NomEtudiant = serializers.CharField()
    CinEtudiant = serializers.CharField()
    NatureStage = serializers.CharField()
    PeriodeStage = serializers.CharField()

    def create(self, validated_data):
        return Stage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.anneeUniversitaire = validated_data.get('anneeUniversitaire', instance.anneeUniversitaire)
        instance.Departement = validated_data.get('Departement', instance.Departement)
        instance.NomEtudiant = validated_data.get('NomEtudiant', instance.NomEtudiant)
        instance.CinEtudiant = validated_data.get('CinEtudiant', instance.CinEtudiant)
        instance.NatureStage = validated_data.get('NatureStage', instance.NatureStage)
        instance.PeriodeStage = validated_data.get('PeriodeStage', instance.PeriodeStage)
        instance.save()
        return instance
