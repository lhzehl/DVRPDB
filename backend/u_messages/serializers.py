from rest_framework import serializers

from .models import StartMessage, ReplyMessage


class StartMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartMessage
        fields = [
            "message",
            "is_read",
            "recipient",
        ]


class ReplyMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyMessage
        fields = [
            "message", "reply_for"
        ]
