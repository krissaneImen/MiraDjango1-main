from rest_framework import serializers
from .models import Seance, EmploiProf
from mongoengine import DoesNotExist

class SeanceSerializer(serializers.Serializer):
    horaire = serializers.CharField(max_length=200)
    matiere = serializers.CharField(max_length=200)
    sale = serializers.CharField(max_length=200)
    jourSemaine = serializers.CharField(max_length=200)
    groupe = serializers.CharField(max_length=20)
    

class EmploiSerializer(serializers.Serializer):
    anneeUniversitaire = serializers.CharField(max_length=200)
    semestre = serializers.CharField(max_length=500)
    NomEnseignant = serializers.CharField(max_length=500)
    CinEnseignant = serializers.CharField(max_length=500)
    type = serializers.CharField(max_length=100)
    Seances = SeanceSerializer(many=True)
    
    def create(self, validated_data):
        seances_data = validated_data.pop('Seances')
        seance = EmploiProf.objects.create(**validated_data)
        for seance_data in seances_data:
            seance.create_seance(**seance_data)
        return seance

   
    def update(self, instance, validated_data):
        instance.anneeUniversitaire = validated_data.get('anneeUniversitaire', instance.anneeUniversitaire)
        instance.semestre = validated_data.get('semestre', instance.semestre)
        instance.NomEnseignant = validated_data.get('NomEnseignant', instance.NomEnseignant)
        instance.CinEnseignant = validated_data.get('CinEnseignant', instance.CinEnseignant)
        instance.type = validated_data.get('type', instance.type)
        instance.save()

        instance.Seances = []

    # Ajouter les nouveaux étudiants
        seances_data = validated_data.get('Seances', [])
        for seance_data in seances_data:
            instance.create_seance(**seance_data)

        instance.save()
        return instance