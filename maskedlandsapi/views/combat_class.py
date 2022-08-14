from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from maskedlandsapi.models import CombatClass


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
            serializer = CombatClassSerializer(combat_class)
            return Response(serializer.data)
        except CombatClass.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle getting all combat_class dictionaries OR all combat_class of a certain type.

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        combat_class = CombatClass.objects.all()
        serializer = CombatClassSerializer(combat_class, many=True)
        return Response(serializer.data)

class CombatClassSerializer(serializers.ModelSerializer):
    """JSON serializer for serializer

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = CombatClass
        fields = ('id', 'name', 'description', 'image_url', 'primary_attribute')