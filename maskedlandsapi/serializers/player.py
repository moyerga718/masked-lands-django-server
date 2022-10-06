from maskedlandsapi.serializers.user import UsernameSerializer
from maskedlandsapi.models import Player
from rest_framework import serializers

class PlayerUsernameSerializer(serializers.ModelSerializer):
    user = UsernameSerializer()
    class Meta:
        model = Player
        fields = ('user',)
        