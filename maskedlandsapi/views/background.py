from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from maskedlandsapi.models import Background
from maskedlandsapi.serializers import BackgroundFilterSerializer


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
            serializer = BackgroundFilterSerializer(background)
            return Response(serializer.data)
        except Background.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle getting all background dictionaries."""

        backgrounds = Background.objects.all()

        serializer = BackgroundFilterSerializer(backgrounds, many=True)
        return Response(serializer.data)