from rest_framework import serializers
from .models import FichePresnce, Etudiant

class EtudiantSerializer(serializers.Serializer):
    NomEtudiant = serializers.CharField(max_length=200)
    Cin = serializers.CharField(max_length=20)
    etatAbscence = serializers.CharField(max_length=20)
    etatElimination = serializers.CharField(max_length=20)

class FichePresnceSerializer(serializers.Serializer):
    nomGroupe = serializers.CharField(max_length=200)
    Seance = serializers.CharField(max_length=500)
    enseignant = serializers.CharField(max_length=500)
    Sale = serializers.CharField(max_length=500)
    DateSeance = serializers.DateField(required=False)
    Matiere = serializers.CharField(max_length=500)
    cinEnseignant = serializers.CharField(max_length=500)
    Anneeuniversitaire = serializers.CharField(max_length=100)
    Etudiants = EtudiantSerializer(many=True)

    def create(self, validated_data):
        etudiants_data = validated_data.pop('Etudiants')
        groupe = FichePresnce.objects.create(**validated_data)
        for etudiant_data in etudiants_data:
            groupe.create_etudiant(**etudiant_data)
        return groupe

    def update(self, instance, validated_data):
        instance.nomGroupe = validated_data.get('nomGroupe', instance.nomGroupe)
        instance.Seance = validated_data.get('Seance', instance.Seance)
        instance.enseignant = validated_data.get('enseignant', instance.enseignant)
        instance.DateSeance = validated_data.get('DateSeance', instance.DateSeance)
        instance.Sale = validated_data.get('Sale', instance.Sale)
        instance.Matiere = validated_data.get('Matiere', instance.Matiere)
        instance.cinEnseignant = validated_data.get('cinEnseignant', instance.cinEnseignant)
        instance.Anneeuniversitaire = validated_data.get('Anneeuniversitaire', instance.Anneeuniversitaire)
        instance.save()

        # Update etudiants
        etudiants_data = validated_data.get('Etudiants', [])
        for etudiant_data in etudiants_data:
            etudiant = instance.get_etudiant_by_Cin(etudiant_data['Cin'])
            if etudiant:
                # Mettre à jour les champs de l'étudiant
                etudiant.NomEtudiant = etudiant_data.get('NomEtudiant', etudiant.NomEtudiant)
                etudiant.etatAbscence = etudiant_data.get('etatAbscence', etudiant.etatAbscence)
                etudiant.etatElimination = etudiant_data.get('etatElimination', etudiant.etatElimination)
        instance.save()

        return instance
