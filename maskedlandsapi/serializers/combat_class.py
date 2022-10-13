from rest_framework import serializers
from maskedlandsapi.models import CombatClass
from maskedlandsapi.serializers.subclass import SubclassFilterSerializer

class CombatClassNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = CombatClass
        fields = ('name',)

class CombatClassFilterSerializer(serializers.ModelSerializer):

    subclasses = SubclassFilterSerializer(many=True)
    class Meta:
        model = CombatClass
        fields = ('id','name','subclasses')