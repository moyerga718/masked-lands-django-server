from rest_framework import serializers
from maskedlandsapi.models import Species

class SpeciesNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Species
        fields = ('name',)