from rest_framework import serializers
from .models import PDFFile

class PDFFileSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    pdf_file = serializers.FileField(required=True)
    type = serializers.CharField(required=False)
    etudiant = serializers.BooleanField(required=False)
    enseignant = serializers.BooleanField(required=False)
    administrateur = serializers.BooleanField(required=False)
    administratif = serializers.BooleanField(required=False)
    

    def create(self, validated_data):
        return PDFFile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.pdf_file = validated_data.get('pdf_file', instance.pdf_file)
        instance.save()
        return instance
