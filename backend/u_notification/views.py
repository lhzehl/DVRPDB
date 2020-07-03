from rest_framework import generics, permissions

from .models import Actions, Notifications

from .serializers import ActionsListSerializers, NotificationsSerializers


class ActionsListView(generics.ListAPIView):
    serializer_class = ActionsListSerializers
    queryset = Actions.objects.all()


class UsersNotificationView(generics.ListAPIView):
    serializer_class = NotificationsSerializers

    # queryset = Notifications.objects.filter(to_users=(request.user.profile,))
    def get_queryset(self):
        return Notifications.objects.filter(to_users=(self.request.user.profile.id,))
