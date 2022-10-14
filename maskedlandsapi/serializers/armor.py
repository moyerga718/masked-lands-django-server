from rest_framework import serializers
from maskedlandsapi.models import Armor


class ArmorDetailedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Armor
        fields = ('id','name','base_ac','dex_bonus','bonus_cap','strength_requirement','image_url')
        depth = 1