from rest_framework_mongoengine import serializers

from .models import Profil

class ProfileSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Profil
        fields = '__all__'


