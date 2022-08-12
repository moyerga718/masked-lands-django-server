from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from maskedlandsapi.models import Character

class CharacterView(ViewSet): 

    def list(self, request):
        """_summary_

        Args:
            request (_type_): _description_
        """

        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ('id','name','player','xp','bio','image_url','species','background','combat_class','subclass','weapon','armor','level')
        depth = 2