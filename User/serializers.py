from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.Serializer):
    cin = serializers.CharField(required=True)
    dateDeDelivrance = serializers.DateTimeField(required=False)
    email = serializers.EmailField(required=True)
    phoneNumber = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    firstName = serializers.CharField(required=False)
    lastName = serializers.CharField(required=False)
    statut = serializers.CharField(required=False)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = User(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.dateDeDelivrance = validated_data.get('dateDeDelivrance', instance.dateDeDelivrance)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.password = make_password(validated_data.get('password', instance.password))
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.titre = validated_data.get('titre', instance.titre)
        instance.statut = validated_data.get('statut', instance.statut)
        instance.save()
        return instance
