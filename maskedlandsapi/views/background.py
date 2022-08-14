from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from maskedlandsapi.models import Background


class BackgroundView(ViewSet):
    """Handle all HTTP Requests for Background

    Args:
        ViewSet (_type_): _description_
    """

    def retrieve(self, request, pk):

        """Handle getting a single background dictionary

        Returns:
            _type_: _description_
        """

        try:
            background = Background.objects.get(pk=pk)
            serializer = BackgroundSerializer(background)
            return Response(serializer.data)
        except Background.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle getting all background dictionaries OR all background of a certain type.

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        backgrounds = Background.objects.all()

        species = request.query_params.get('species', None)
        if species is not None:
            backgrounds = backgrounds.filter(species=species)


        serializer = BackgroundSerializer(backgrounds, many=True)
        return Response(serializer.data)

class BackgroundSerializer(serializers.ModelSerializer):
    """JSON serializer for serializer

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = Background
        fields = ('id', 'name', 'description', 'image_url', 'species')