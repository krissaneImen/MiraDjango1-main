from rest_framework import serializers
from .models import TypeReglement




class TypeReglementSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    cible = serializers.CharField(required=True)
    
    def create(self, validated_data):
        reglement = TypeReglement(**validated_data)
        reglement.save()
        return reglement

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cible = validated_data.get('cible', instance.cible)
        instance.save()
        return instance
