from rest_framework import serializers, pagination
from api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'name', 'phone', 'api_key', 'status', 'created_at', 'gcm_registration_id', 'profile_image')


