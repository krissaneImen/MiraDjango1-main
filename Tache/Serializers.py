from rest_framework import serializers
from .models import Tache

class TacheSerializer(serializers.Serializer):
    idJournale = serializers.CharField()
    TacheJournaliere = serializers.CharField()
    Date = serializers.DateField()
    LastModified = serializers.DateField()
   
   
    def create(self, validated_data):
        return Tache.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.TacheJournaliere = validated_data.get('TacheJournaliere', instance.TacheJournaliere)
        instance.Date = validated_data.get('Date', instance.Date)
        instance.LastModified = validated_data.get('LastModified', instance.LastModified)
        instance.save()
        return instance
