from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from maskedlandsapi.models import CombatClass
from maskedlandsapi.serializers import CombatClassFilterSerializer


class CombatClassView(ViewSet):
    """Handle all HTTP Requests for CombatClass

    Args:
        ViewSet (_type_): _description_
    """

    def retrieve(self, request, pk):

        """Handle getting a single combat_class dictionary

        Returns:
            _type_: _description_
        """

        try:
            combat_class = CombatClass.objects.get(pk=pk)
            serializer = CombatClassFilterSerializer(combat_class)
            return Response(serializer.data)
        except CombatClass.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle getting all combat_class dictionaries.

        """
        combat_class = CombatClass.objects.all()
        
        serializer = CombatClassFilterSerializer(combat_class, many=True)
        return Response(serializer.data)