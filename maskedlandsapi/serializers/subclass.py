from rest_framework import serializers
from maskedlandsapi.models import Subclass

class SubclassNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subclass
        fields = ('name',)