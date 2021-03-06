from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status

from .models import Dialog, Reply
from .serializers import StartMessageSerializer, ReplyMessageSerializer, DialogDetailSerializer, DialogListSerializer

from rest_framework import permissions


class IsSenderOrIsRecipient(permissions.BasePermission):
    """
    permission check is current user message author or message recipient

    """

    def has_object_permission(self, request, view, obj):
        try:
            is_sender = request.user.profile == obj.sender

            is_recipient = request.user.profile == obj.recipient
        except AttributeError:
            is_sender = request.user.profile == obj.dialog.sender

            is_recipient = request.user.profile == obj.dialog.recipient
        # except

        has_permission = is_sender or is_recipient

        return has_permission


class StartMessageView(generics.CreateAPIView):
    """
    Start dialog
    """
    serializer_class = StartMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user.profile)


class ReplyMessageView(generics.CreateAPIView):
    """
    Reply for message
    """
    serializer_class = ReplyMessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsSenderOrIsRecipient]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user.profile)


class SDialogListView(generics.ListAPIView):
    """
    start by user dialog
    """

    serializer_class = DialogListSerializer
    permission_classes = [permissions.IsAuthenticated, IsSenderOrIsRecipient]

    def get_queryset(self):
        """
        for anonimus user return error
        :return:
        """
        try:
            user = self.request.user.profile
        except AttributeError:
            return []
        return Dialog.objects.filter(sender=user)


class RDialogListView(generics.ListAPIView):
    """
    user recipient dialog list
    """

    serializer_class = DialogListSerializer
    permission_classes = [permissions.IsAuthenticated, IsSenderOrIsRecipient]

    def get_queryset(self):
        try:
            user = self.request.user.profile
        except AttributeError:
            return []
        return Dialog.objects.filter(recipient=user)


class DialogDetailView(generics.RetrieveAPIView):
    serializer_class = DialogDetailSerializer
    queryset = Dialog.objects.all()

    permission_classes = [permissions.IsAuthenticated, IsSenderOrIsRecipient]
