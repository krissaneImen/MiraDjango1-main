from rest_framework import serializers
from .models import DetailJournale

class DetailJournaleSerializer(serializers.Serializer):
    anneeUniversitaire = serializers.CharField(max_length=200)
    Nom = serializers.CharField(max_length=500)
    Cin = serializers.CharField(max_length=500)
    Prenom = serializers.CharField(max_length=500)
    Departement = serializers.CharField(max_length=1000)
    Option = serializers.CharField(max_length=1000)
    Entreprise = serializers.CharField(max_length=1000)
    Adress = serializers.CharField(max_length=1000)
    Fax = serializers.CharField(max_length=1000)
    NatureStage = serializers.CharField(max_length=1000)
    PeriodeStage = serializers.CharField(max_length=1000)
    etatEvaluation = serializers.CharField(required=False)
   
    def create(self, validated_data):
        return DetailJournale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.anneeUniversitaire = validated_data.get('anneeUniversitaire', instance.anneeUniversitaire)
        instance.Nom = validated_data.get('Nom', instance.Nom)
        instance.Cin = validated_data.get('Cin', instance.Cin)
        instance.Prenom = validated_data.get('Prenom', instance.Prenom)
        instance.Departement = validated_data.get('Departement', instance.Departement)
        instance.Option = validated_data.get('Option', instance.Option)
        instance.Entreprise = validated_data.get('Entreprise', instance.Entreprise)
        instance.Adress = validated_data.get('Adress', instance.Adress)
        instance.Fax = validated_data.get('Fax', instance.Fax)
        instance.NatureStage = validated_data.get('NatureStage', instance.NatureStage)
        instance.PeriodeStage = validated_data.get('PeriodeStage', instance.PeriodeStage)
        instance.etatEvaluation = validated_data.get('etatEvaluation', instance.etatEvaluation)
        instance.save()
        return instance
