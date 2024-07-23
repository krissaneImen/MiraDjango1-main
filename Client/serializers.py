from rest_framework import serializers
from .models import Institut
from mongoengine import DoesNotExist

class ContactSerializer(serializers.Serializer):
    nom = serializers.CharField()
    valeur = serializers.CharField()

class SocialSerializer(serializers.Serializer):
    url = serializers.CharField()
    icon = serializers.CharField()

class InstitutSerializer(serializers.Serializer):
    nomInstitut = serializers.CharField()
    acronyme = serializers.CharField()
    Directeur = serializers.CharField()
    logo = serializers.CharField(default='')
    Contacts = ContactSerializer(many=True)
    Socials = SocialSerializer(many=True)

    def create(self, validated_data):
        contacts_data = validated_data.pop('Contacts')
        socials_data = validated_data.pop('Socials')
        institut = Institut.objects.create(**validated_data)
        for social_data in socials_data:
            institut.create_social(**social_data)

        for contact_data in contacts_data:
            institut.create_contact(**contact_data)
        return institut

    def update(self, instance, validated_data):
        instance.nomInstitut = validated_data.get('nomInstitut', instance.nomInstitut)
        instance.acronyme = validated_data.get('acronyme', instance.acronyme)
        instance.Directeur = validated_data.get('Directeur', instance.Directeur)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.save()

        instance.Socials = []
        instance.Contacts = []

        # Add new socials
        socials_data = validated_data.get('Socials', [])
        for social_data in socials_data:
            instance.create_social(**social_data)

        # Add new contacts
        contacts_data = validated_data.get('Contacts', [])
        for contact_data in contacts_data:
            instance.create_contact(**contact_data)

        instance.save()
        return instance
