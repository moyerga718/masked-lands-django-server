from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers

class UsernameSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('username',)