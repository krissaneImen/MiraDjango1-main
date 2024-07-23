from rest_framework import serializers
from .models import Demande

class DemandeSerializer(serializers.Serializer):
    Demande = serializers.CharField(required=True)
    Responsable = serializers.CharField(required=True)
    Cin = serializers.CharField(required=True)
    DateDemande = serializers.DateTimeField(required=False)
    PretLe = serializers.DateTimeField(required=False)
    Etat = serializers.CharField(required=True)

    def create(self, validated_data):
        demande = Demande(**validated_data)
        demande.save()
        return demande

    def update(self, instance, validated_data):
        instance.Demande = validated_data.get('Demande', instance.Demande)
        instance.Responsable = validated_data.get('Responsable', instance.Responsable)
        instance.Cin = validated_data.get('Cin', instance.Cin)
        instance.DateDemande = validated_data.get('DateDemande', instance.DateDemande)
        instance.PretLe = validated_data.get('PretLe', instance.PretLe)
        instance.Etat = validated_data.get('Etat', instance.Etat)
        instance.save()
        return instance
