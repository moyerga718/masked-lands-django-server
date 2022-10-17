from rest_framework import serializers
from maskedlandsapi.models import Species
from maskedlandsapi.serializers.background import BackgroundFilterSerializer

class SpeciesNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Species
        fields = ('name','speed')

class SpeciesFilterSerializer(serializers.ModelSerializer):

    backgrounds = BackgroundFilterSerializer(many=True)
    class Meta:
        model = Species
        fields = ('id','name','backgrounds')