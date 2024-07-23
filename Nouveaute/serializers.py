from rest_framework import serializers
from .models import Nouveaute
from django.utils import timezone

class NouveauteSerializer(serializers.Serializer):
    Identifiant = serializers.CharField(required=True)
    anneeUniversitaire = serializers.CharField(default='')
    date = serializers.DateTimeField(default=timezone.now)
    intitule = serializers.CharField(max_length=150, required=True)
    etudiant = serializers.BooleanField(default=False)  # Nouveau champ "etudiant"
    enseignant = serializers.BooleanField(default=False)  # Nouveau champ "enseignant"
    administratif = serializers.BooleanField(default=False)  # Nouveau champ "administratif"
    administrateur = serializers.BooleanField(default=False)  # Nouveau champ "administrateur"
    image = serializers.CharField(default='')
    

    def create(self, validated_data):
        return Nouveaute.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.anneeUniversitaire = validated_data.get('anneeUniversitaire', instance.anneeUniversitaire)
        instance.date = validated_data.get('date', instance.date)
        instance.intitule = validated_data.get('intitule', instance.intitule)
        instance.etudiant = validated_data.get('etudiant', instance.etudiant)     # Mise à jour du champ "etudiant"
        instance.enseignant = validated_data.get('enseignant', instance.enseignant)  # Mise à jour du champ "enseignant"
        instance.administratif = validated_data.get('administratif', instance.administratif)  # Mise à jour du champ "administratif"
        instance.administrateur = validated_data.get('administrateur', instance.administrateur)  # Mise à jour du champ "administrateur"
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
