from rest_framework import serializers
from .models import Formation

class FormationSerializer(serializers.Serializer):
    Identifiant = serializers.CharField(required=True)
    intitule = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    dateDeFormation = serializers.DateField(required=False)
    lieuFormation = serializers.CharField(required=False)
    datePublication = serializers.DateField(required=False)
    responsable = serializers.CharField(required=False)
    formateur = serializers.CharField(required=False)
    lienInscription = serializers.CharField(required=False)
    phoneNumber = serializers.CharField(required=True)
    poster = serializers.CharField(default='')
    codeQrInscription = serializers.CharField(default='')
    etudiant = serializers.BooleanField(default=False)  # Nouveau champ "etudiant"
    enseignant = serializers.BooleanField(default=False)  # Nouveau champ "enseignant"
    administratif = serializers.BooleanField(default=False)  # Nouveau champ "administratif"
    administrateur = serializers.BooleanField(default=False)  # Nouveau champ "administrateur"

    def create(self, validated_data):
        formation = Formation(**validated_data)
        formation.save()
        return formation

    def update(self, instance, validated_data):
        instance.intitule = validated_data.get('intitule', instance.intitule)
        instance.description = validated_data.get('description', instance.description)
        instance.dateDeFormation = validated_data.get('dateDeFormation', instance.dateDeFormation)
        instance.datePublication = validated_data.get('datePublication', instance.datePublication)
        instance.lieuFormation = validated_data.get('lieuFormation', instance.lieuFormation)
        instance.responsable = validated_data.get('responsable', instance.responsable)
        instance.formateur = validated_data.get('formateur', instance.formateur)
        instance.lienInscription = validated_data.get('lienInscription', instance.lienInscription)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.poster = validated_data.get('poster', instance.poster)
        instance.codeQrInscription = validated_data.get('codeQrInscription', instance.codeQrInscription)
        instance.etudiant = validated_data.get('etudiant', instance.etudiant)     # Mise à jour du champ "etudiant"
        instance.enseignant = validated_data.get('enseignant', instance.enseignant)  # Mise à jour du champ "enseignant"
        instance.administratif = validated_data.get('administratif', instance.administratif)  # Mise à jour du champ "administratif"
        instance.administrateur = validated_data.get('administrateur', instance.administrateur)  # Mise à jour du champ "administrateur"
        instance.save()
        return instance
