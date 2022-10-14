from rest_framework import serializers
from maskedlandsapi.models import Weapon


class WeaponDetailedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weapon
        fields = ('id','name','attribute','damage_die','number_of_damage_die','image_url')
        depth = 1