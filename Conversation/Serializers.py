from rest_framework import serializers
from .models import  Conversation
from mongoengine import DoesNotExist

class MessageSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=200)
    Contenu = serializers.CharField()
    heure = serializers.CharField()
    dateConversation = serializers.DateField()
    

class ConversationSerializer(serializers.Serializer):
    Titre = serializers.CharField(max_length=200)
    CinUser = serializers.CharField(max_length=200)
    dateConversation = serializers.CharField()
    Messages = MessageSerializer(many=True)
    
    def create(self, validated_data):
        messages_data = validated_data.pop('Messages')
        conversation = Conversation.objects.create(**validated_data)
        for message_data in messages_data:
            conversation.create_message(**message_data)
        return conversation

   
    def update(self, instance, validated_data):
        instance.Titre = validated_data.get('Titre', instance.Titre)
        instance.CinUser = validated_data.get('CinUser', instance.CinUser)
        instance.dateConversation = validated_data.get('dateConversation', instance.dateConversation)
        instance.save()

        instance.Messges = []

    # Ajouter les nouveaux étudiants
        messages_data = validated_data.get('Messages', [])
        for message_data in messages_data:
            instance.create_message(**message_data)

        instance.save()
        return instance