from rest_framework import serializers
from .models import Profil



class ProfileSignUpSerializer(serializers.Serializer):
    cartCin = serializers.CharField(max_length=20, required=True)
    firstName = serializers.CharField(max_length=150, required=False)
    lastName = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=True)
    phoneNumber = serializers.CharField(required=True)
    dateDeDelivrance = serializers.DateField(default=None)
    prenom_arabe = serializers.CharField(max_length=150, default='')
    nomArabe = serializers.CharField(max_length=150, default='')
    lieuNaissanceArabe = serializers.CharField(max_length=100, default='')
    adresseArabe = serializers.CharField(required=False, default='')
    delegationArabe = serializers.CharField(max_length=100, default='')
    genre = serializers.CharField(max_length=10, default='')
    etatCivil = serializers.CharField(max_length=20, default='')
    nationalite = serializers.CharField(max_length=100, default='')
    dateNaissance = serializers.DateField(default=None)
    lieuNaissance = serializers.CharField(max_length=100, default='')
    adresse = serializers.CharField(default='')
    gouvernorat = serializers.CharField(max_length=100, default='')
    delegation = serializers.CharField(max_length=100, default='')
    codePostal = serializers.CharField(max_length=10, default='')
    image = serializers.CharField(default='')
    
    

    def create(self, validated_data):
        profile = Profil(**validated_data)
        profile.save()
        return profile

    def update(self, instance, validated_data):
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.prenom_arabe = validated_data.get('prenom_arabe', instance.prenom_arabe)
        instance.nomArabe = validated_data.get('nomArabe', instance.nomArabe)
        instance.lieuNaissanceArabe = validated_data.get('lieuNaissanceArabe', instance.lieuNaissanceArabe)
        instance.adresseArabe = validated_data.get('adresseArabe', instance.adresseArabe)
        instance.delegationArabe = validated_data.get('delegationArabe', instance.delegationArabe)
        instance.dateDeDelivrance = validated_data.get('dateDeDelivrance', instance.dateDeDelivrance)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.etatCivil = validated_data.get('etatCivil', instance.etatCivil)
        instance.nationalite = validated_data.get('nationalite', instance.nationalite)
        instance.dateNaissance = validated_data.get('dateNaissance', instance.dateNaissance)
        instance.lieuNaissance = validated_data.get('lieuNaissance', instance.lieuNaissance)
        instance.adresse = validated_data.get('adresse', instance.adresse)
        instance.gouvernorat = validated_data.get('gouvernorat', instance.gouvernorat)
        instance.delegation = validated_data.get('delegation', instance.delegation)
        instance.codePostal = validated_data.get('codePostal', instance.codePostal)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
