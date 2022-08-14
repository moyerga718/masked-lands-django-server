from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from maskedlandsapi.models import Armor


class ArmorView(ViewSet):
    """Handle all HTTP Requests for Armor

    Args:
        ViewSet (_type_): _description_
    """

    def retrieve(self, request, pk):

        """Handle getting a single armor dictionary

        Returns:
            _type_: _description_
        """

        try:
            armor = Armor.objects.get(pk=pk)
            serializer = ArmorSerializer(armor)
            return Response(serializer.data)
        except Armor.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle geting all armor dictionaries OR all armor of a certain type.

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        armor = Armor.objects.all()

        #FILTER BY ARMOR TYPE CODE BLOCK
        armor_type = request.query_params.get('armor_type', None)
        if armor_type is not None:
            armor = armor.filter(armor_type=armor_type)

        serializer = ArmorSerializer(armor, many=True)
        return Response(serializer.data)

class ArmorSerializer(serializers.ModelSerializer):
    """JSON serializer for armor

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = Armor
        fields = ('id', 'name', 'base_ac', 'dex_bonus', 'bonus_cap', 'strength_requirement', 'image_url', 'armor_type')