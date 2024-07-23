from rest_framework import serializers
from .models import Manifestation

class ManifestationSerializer(serializers.Serializer):
    Identifiant = serializers.CharField(required=False)
    intitule = serializers.CharField(required=True)
    slogan = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    dateDebut = serializers.DateField(required=False)
    dateFin = serializers.DateField(required=False)
    lieuManifestation = serializers.CharField(required=False)
    responsables = serializers.CharField(required=False)
    formateurs = serializers.CharField(required=False)
    phoneNumber = serializers.CharField(required=False)
    prix = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    poster = serializers.CharField(default='')
    categorie = serializers.CharField(required=False)  # Nouveau champ "categorie"
    lien = serializers.CharField(required=False)        # Nouveau champ "lien"
    etudiant = serializers.BooleanField(default=False)  # Nouveau champ "etudiant"
    enseignant = serializers.BooleanField(default=False)  # Nouveau champ "enseignant"
    administratif = serializers.BooleanField(default=False)  # Nouveau champ "administratif"
    administrateur = serializers.BooleanField(default=False)  # Nouveau champ "administrateur"

    def create(self, validated_data):
        return Manifestation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.intitule = validated_data.get('intitule', instance.intitule)
        instance.slogan = validated_data.get('slogan', instance.slogan)
        instance.description = validated_data.get('description', instance.description)
        instance.dateDebut = validated_data.get('dateDebut', instance.dateDebut)
        instance.lieuManifestation = validated_data.get('lieuManifestation', instance.lieuManifestation)
        instance.dateFin = validated_data.get('dateFin', instance.dateFin)
        instance.responsables = validated_data.get('responsables', instance.responsables)
        instance.formateurs = validated_data.get('formateurs', instance.formateurs)
        instance.lienInscription = validated_data.get('lienInscription', instance.lienInscription)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.poster = validated_data.get('poster', instance.poster)
        instance.categorie = validated_data.get('categorie', instance.categorie)  # Mise à jour du champ "categorie"
        instance.prix = validated_data.get('prix', instance.prix)                 # Mise à jour du champ "prix"
        instance.email = validated_data.get('email', instance.email)                 # Mise à jour du champ "prix"
        instance.lien = validated_data.get('lien', instance.lien)                 # Mise à jour du champ "lien"
        instance.etudiant = validated_data.get('etudiant', instance.etudiant)     # Mise à jour du champ "etudiant"
        instance.enseignant = validated_data.get('enseignant', instance.enseignant)  # Mise à jour du champ "enseignant"
        instance.administratif = validated_data.get('administratif', instance.administratif)  # Mise à jour du champ "administratif"
        instance.administrateur = validated_data.get('administrateur', instance.administrateur)  # Mise à jour du champ "administrateur"
        instance.save()
        return instance
