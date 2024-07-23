from rest_framework import serializers
from .models import Etudiant, Soutenance
from mongoengine import DoesNotExist

class EtudiantSerializer(serializers.Serializer):
    NomEtudiant = serializers.CharField(max_length=200)
    Cin = serializers.CharField(max_length=20)
    

class SoutenanceSerializer(serializers.Serializer):
    NomRaporteur = serializers.CharField(max_length=200)
    CinRaporteur = serializers.CharField(max_length=500)
    NomPresidentJuri = serializers.CharField(max_length=500)
    CinPresidentJuri = serializers.CharField(max_length=500)
    NomEncadreur = serializers.CharField(max_length=100)
    CinEncadreur = serializers.CharField(max_length=100)
    NatureStage = serializers.CharField(max_length=100)
    Anneeuniversitaire = serializers.CharField(max_length=100)
    dateJury = serializers.DateField()
    Etudiants = EtudiantSerializer(many=True)
    
    def create(self, validated_data):
        etudiants_data = validated_data.pop('Etudiants')
        soutenance = Soutenance.objects.create(**validated_data)
        for etudiant_data in etudiants_data:
            soutenance.create_etudiant(**etudiant_data)
        return soutenance

   
    def update(self, instance, validated_data):
        instance.NomRaporteur = validated_data.get('NomRaporteur', instance.NomRaporteur)
        instance.CinRaporteur = validated_data.get('CinRaporteur', instance.CinRaporteur)
        instance.NomPresidentJuri = validated_data.get('NomPresidentJuri', instance.NomPresidentJuri)
        instance.CinPresidentJuri = validated_data.get('CinPresidentJuri', instance.CinPresidentJuri)
        instance.NomEncadreur = validated_data.get('NomEncadreur', instance.NomEncadreur)
        instance.CinEncadreur = validated_data.get('CinEncadreur', instance.CinEncadreur)
        instance.NatureStage = validated_data.get('NatureStage', instance.NatureStage)
        instance.dateJury = validated_data.get('dateJury', instance.dateJury)
        instance.Anneeuniversitaire = validated_data.get('Anneeuniversitaire', instance.Anneeuniversitaire)
        instance.save()

        instance.Etudiants = []

    # Ajouter les nouveaux étudiants
        etudiants_data = validated_data.get('Etudiants', [])
        for etudiant_data in etudiants_data:
            instance.create_etudiant(**etudiant_data)

        instance.save()
        return instance