from rest_framework import serializers

from .models import Actions, Notifications
from users.models import Profile


class ByUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'username'
        ]


class ActionsListSerializers(serializers.ModelSerializer):
    by_user = ByUserSerializers()

    class Meta:
        model = Actions
        fields = '__all__'


class NotificationsSerializers(serializers.ModelSerializer):
    actions = ActionsListSerializers()

    class Meta:
        model = Notifications
        fields = ['actions']
