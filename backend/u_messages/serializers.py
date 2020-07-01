from rest_framework import serializers

from .models import StartMessage, ReplyMessage


class StartMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartMessage
        fields = '__all__'


class ReplyMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyMessage
        fields = '__all__'