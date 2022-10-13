from rest_framework import serializers
from maskedlandsapi.models import Background

class BackgroundNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Background
        fields = ('name',)

class BackgroundFilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Background
        fields = ('id','name',)
        