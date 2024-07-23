from rest_framework import serializers
from .models import Attestation

class AttestationSerializer(serializers.Serializer):
    Nom = serializers.CharField(required=True)
    type = serializers.CharField(required=False)
    idDemande = serializers.CharField(required=True)
    Cin = serializers.CharField(required=True)
    Etat = serializers.CharField(required=True)
    
    def create(self, validated_data):
        attestation = Attestation(**validated_data)
        attestation.save()
        return attestation

    def update(self, instance, validated_data):
        instance.Nom = validated_data.get('Nom', instance.Nom)
        instance.type = validated_data.get('type', instance.type)
        instance.idDemande = validated_data.get('idDemande', instance.idDemande)
        instance.Cin = validated_data.get('Cin', instance.Cin)
        instance.Etat = validated_data.get('Etat', instance.Etat)
        instance.save()
        return instance
