from rest_framework import serializers
from maskedlandsapi.models import Character

from maskedlandsapi.serializers.species import SpeciesNameSerializer
from maskedlandsapi.serializers.background import BackgroundNameSerializer
from maskedlandsapi.serializers.combat_class import CombatClassNameSerializer
from maskedlandsapi.serializers.subclass import SubclassNameSerializer
from maskedlandsapi.serializers.player import PlayerUsernameSerializer

class CharacterCardSerializer(serializers.ModelSerializer):
    species = SpeciesNameSerializer()
    background = BackgroundNameSerializer()
    combat_class = CombatClassNameSerializer()
    subclass = SubclassNameSerializer()
    player = PlayerUsernameSerializer()
    class Meta:
        model = Character
        fields = ('id','name','player','image_url','species','background','combat_class','subclass','level')