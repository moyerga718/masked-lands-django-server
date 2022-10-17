from rest_framework import serializers
from maskedlandsapi.models import Spell

class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = ('name','god','devotion_level','short_description','full_description','action_type','will_cost','attack_range')