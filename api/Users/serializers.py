from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=['id', 'username', 'email', 'photo']
        extra_kwargs = {'password': {'write_only': True}}