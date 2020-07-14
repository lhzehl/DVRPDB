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


class DialogItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyMessage
        fields = [
            "sender", "message", 'id'
        ]


class DialogDetailSerializer(serializers.ModelSerializer):
    replymessage = DialogItemsSerializer(read_only=True, many=True)
    class Meta:
        model = StartMessage
        fields = [
            "message","sender", 
            "recipient",'replymessage'
        ]