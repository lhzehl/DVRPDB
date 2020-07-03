from rest_framework import serializers

from .models import Profile, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserInProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'last_login', 'is_superuser', 'is_staff',
            'is_active', 'date_joined', 'groups'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserInProfileSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id', 'image', 'name',
            'username', 'dob', 'new_notification',
            'user'
        ]