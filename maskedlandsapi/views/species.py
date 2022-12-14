from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from maskedlandsapi.models import Species
from maskedlandsapi.serializers.species import SpeciesFilterSerializer


class SpeciesView(ViewSet):
    """Handle all HTTP Requests for Species

    Args:
        ViewSet (_type_): _description_
    """

    def retrieve(self, request, pk):

        """Handle getting a single species dictionary

        Returns:
            _type_: _description_
        """

        try:
            species = Species.objects.get(pk=pk)
            serializer = SpeciesFilterSerializer(species)
            return Response(serializer.data)
        except Species.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle geting all species dictionaries OR all species of a certain type.

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        species = Species.objects.all()
        serializer = SpeciesFilterSerializer(species, many=True)
        return Response(serializer.data)