from rest_framework import serializers

from .models import Actions, Notifications, \
    SubscriptionForUser, SubscriptionForPost, SubscriptionForCategory

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


class SubscriptionForUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionForUser
        fields = ['object_of_observation']


class SubscriptionForPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionForPost
        fields = ['object_of_observation']


class SubscriptionForCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionForCategory
        fields = ['object_of_observation']


class SubToUsersList(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionForUser
        fields = '__all__'