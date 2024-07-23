from rest_framework import serializers
from .models import Avis

class AvisSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=500)
    enseignant = serializers.CharField(max_length=500)
    cinEnseignant = serializers.CharField(max_length=500)
    heureDebut = serializers.CharField(max_length=500,required=False)
    heureFin = serializers.CharField(max_length=500,required=False)
    etat = serializers.CharField(max_length=500)
    DateAvis = serializers.CharField(max_length=500,required=False)
    Datefin = serializers.CharField(max_length=500, required=False)
    Anneeuniversitaire = serializers.CharField(max_length=100)
    Classes = serializers.ListField(child=serializers.CharField(max_length=200), required=False)

    def create(self, validated_data):
        return Avis.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.etat = validated_data.get('etat', instance.etat)
        instance.enseignant = validated_data.get('enseignant', instance.enseignant)
        instance.cinEnseignant = validated_data.get('cinEnseignant', instance.cinEnseignant)
        instance.heureDebut = validated_data.get('heureDebut', instance.heureDebut)
        instance.heureFin = validated_data.get('heureFin', instance.heureFin)
        instance.DateAvis = validated_data.get('DateAvis', instance.DateAvis)
        instance.Datefin = validated_data.get('Datefin', instance.Datefin)
        instance.Anneeuniversitaire = validated_data.get('Anneeuniversitaire', instance.Anneeuniversitaire)
        instance.Classes = validated_data.get('Classes', instance.Classes)
        instance.save()
        return instance