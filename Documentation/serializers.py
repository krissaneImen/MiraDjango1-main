from rest_framework import serializers
from .models import Reglement


class ReglementSerializer(serializers.Serializer):
    identifiant = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    type = serializers.CharField(required=True)
    etudiant = serializers.BooleanField(required=False)
    enseignant = serializers.BooleanField(required=False)
    administrateur = serializers.BooleanField(required=False)
    administratif = serializers.BooleanField(required=False)
    
    
    def create(self, validated_data):
        reglement = Reglement(**validated_data)
        reglement.save()
        return reglement

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance


