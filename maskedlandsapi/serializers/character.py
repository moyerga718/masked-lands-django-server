from rest_framework import serializers
from maskedlandsapi.models import Character
from maskedlandsapi.serializers.armor import ArmorDetailedSerializer

from maskedlandsapi.serializers.species import SpeciesNameSerializer
from maskedlandsapi.serializers.background import BackgroundNameSerializer
from maskedlandsapi.serializers.combat_class import CombatClassNameSerializer
from maskedlandsapi.serializers.subclass import SubclassNameSerializer
from maskedlandsapi.serializers.player import PlayerUsernameSerializer
from maskedlandsapi.serializers.weapon import WeaponDetailedSerializer

class CharacterCardSerializer(serializers.ModelSerializer):
    species = SpeciesNameSerializer()
    background = BackgroundNameSerializer()
    combat_class = CombatClassNameSerializer()
    subclass = SubclassNameSerializer()
    player = PlayerUsernameSerializer()
    class Meta:
        model = Character
        fields = ('id','name','player','image_url','species','background','combat_class','subclass','level')

class CharacterSheetSerializer(serializers.ModelSerializer):
    species = SpeciesNameSerializer()
    background = BackgroundNameSerializer()
    combat_class = CombatClassNameSerializer()
    subclass = SubclassNameSerializer()
    player = PlayerUsernameSerializer()
    weapon = WeaponDetailedSerializer()
    armor = ArmorDetailedSerializer()
    class Meta:
        model = Character
        fields = ('id','name','player','bio','image_url',
        'max_life','max_will','max_stamina','hit_die',
        'species','background','combat_class','subclass',
        'level','weapon','armor','ac',
        'eff_strength','eff_dexterity','eff_constitution','eff_intelligence','eff_attunement','eff_charisma',
        'str_mod','dex_mod','con_mod','int_mod','att_mod','cha_mod',
        'sunface_pts','moonface_pts','escritorio_pts','goge_pts','faelina_pts','garthank_pts',
        'sunface_lvl','moonface_lvl','escritorio_lvl','goge_lvl','faelina_lvl','garthank_lvl')