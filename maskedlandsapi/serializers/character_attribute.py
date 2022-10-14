from rest_framework import serializers
from maskedlandsapi.models import CharacterAttribute

class CharacterAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterAttribute
        fields = ('attribute','value')
        depth = 1