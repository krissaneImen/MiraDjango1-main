from rest_framework import serializers
from .models import Files

class FilesSerializer(serializers.Serializer):
    pdf = serializers.FileField()

    def create(self, validated_data):
        return Files.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pdf = validated_data.get('pdf', instance.pdf)
        instance.save()
        return instance
