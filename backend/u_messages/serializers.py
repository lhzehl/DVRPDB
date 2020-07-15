from rest_framework import serializers

from .models import Dialog, Reply
from users.models import Profile as Sender


class MessageAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sender
        fields = [
            'id', 'username', 'image'
        ]


class StartMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialog
        fields = [
            "message",
            'id',
            # "is_read",
            "recipient",
        ]


class ReplyMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = [
            "message", "dialog"
        ]


class DialogItemsSerializer(serializers.ModelSerializer):
    sender = MessageAuthorSerializer()

    class Meta:
        model = Reply
        fields = [
            "sender", "message", 'id', "date_add"
        ]


class DialogDetailSerializer(serializers.ModelSerializer):
    sender = MessageAuthorSerializer(read_only=True)
    recipient = MessageAuthorSerializer(read_only=True)
    reply = DialogItemsSerializer(read_only=True, many=True)

    class Meta:
        model = Dialog
        fields = [
            "message", "sender",
            "recipient", "reply", 'id'
        ]

class DialogListSerializer(serializers.ModelSerializer):
    sender = MessageAuthorSerializer(read_only=True)
    recipient = MessageAuthorSerializer(read_only=True)
    class Meta:
        model = Dialog
        fields = [
            'id',
            'sender',
            "message",
            "is_read",
            "recipient",
        ]