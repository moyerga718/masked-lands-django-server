from rest_framework import serializers
from maskedlandsapi.models import CombatClass

class CombatClassNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = CombatClass
        fields = ('name',)