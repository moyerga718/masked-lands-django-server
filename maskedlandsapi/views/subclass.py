from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from maskedlandsapi.models import Subclass
from maskedlandsapi.serializers.subclass import SubclassFilterSerializer


class SubclassView(ViewSet):
    """Handle all HTTP Requests for Subclass

    Args:
        ViewSet (_type_): _description_
    """

    def retrieve(self, request, pk):

        """Handle getting a single subclass dictionary

        Returns:
            _type_: _description_
        """

        try:
            subclass = Subclass.objects.get(pk=pk)
            serializer = SubclassSerializer(subclass)
            return Response(serializer.data)
        except Subclass.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle getting all subclass dictionaries OR all subclass of a certain type.
        """
        subclasses = Subclass.objects.all()

        serializer = SubclassFilterSerializer(subclasses, many=True)
        return Response(serializer.data)

class SubclassSerializer(serializers.ModelSerializer):
    """JSON serializer for serializer

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = Subclass
        fields = ('id', 'name', 'hit_die', 'life', 'will', 'will_per_level', 'stamina', 'stamina_per_level', 'devotion_points', 'description', 'image_url', 'combat_class')