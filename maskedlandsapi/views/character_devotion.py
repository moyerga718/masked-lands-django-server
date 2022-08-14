from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from maskedlandsapi.models import CharacterDevotion

class CharacterDevotionView(ViewSet):
    """Handles Devotion http requests.
    """
    def list(self, request):
        """Get all character devotion dictionaries or just devotion for one character"""

        devotion = CharacterDevotion.objects.all()

        #FILTER BY CHARACTER ID CODE BLOCK
        character = request.query_params.get('character', None)
        if character is not None:
            devotion = devotion.filter(character=character)

        serializer = CharacterDevotionSerializer(devotion, many=True)
        return Response(serializer.data)

class CharacterDevotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterDevotion
        fields = ('id', 'devotion_points', 'devotion_level', 'character', 'god')
