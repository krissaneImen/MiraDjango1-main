from rest_framework import serializers
from .models import Etudiant, Groupe
from mongoengine import DoesNotExist

class EtudiantSerializer(serializers.Serializer):
    NomEtudiant = serializers.CharField(max_length=200)
    Cin = serializers.CharField(max_length=20)
    

class GroupeSerializer(serializers.Serializer):
    nomGroupe = serializers.CharField(max_length=200)
    Licence = serializers.CharField(max_length=500)
    Niveau = serializers.CharField(max_length=500)
    Specialite = serializers.CharField(max_length=500)
    Anneeuniversitaire = serializers.CharField(max_length=100)
    Etudiants = EtudiantSerializer(many=True)
    
    def create(self, validated_data):
        etudiants_data = validated_data.pop('Etudiants')
        groupe = Groupe.objects.create(**validated_data)
        for etudiant_data in etudiants_data:
            groupe.create_etudiant(**etudiant_data)
        return groupe

   
    def update(self, instance, validated_data):
        instance.nomGroupe = validated_data.get('nomGroupe', instance.nomGroupe)
        instance.Licence = validated_data.get('Licence', instance.Licence)
        instance.Niveau = validated_data.get('Niveau', instance.Niveau)
        instance.Specialite = validated_data.get('Specialite', instance.Specialite)
        instance.Anneeuniversitaire = validated_data.get('Anneeuniversitaire', instance.Anneeuniversitaire)
        instance.save()

        instance.Etudiants = []

    # Ajouter les nouveaux étudiants
        etudiants_data = validated_data.get('Etudiants', [])
        for etudiant_data in etudiants_data:
            instance.create_etudiant(**etudiant_data)

        instance.save()
        return instance