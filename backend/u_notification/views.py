from rest_framework import generics, permissions

from .models import Actions, Notifications

from .serializers import ActionsListSerializers, NotificationsSerializers, \
    SubscriptionForUserSerializers, SubscriptionForCategorySerializers, SubscriptionForPostSerializers


class ActionsListView(generics.ListAPIView):
    serializer_class = ActionsListSerializers
    queryset = Actions.objects.all()


class UsersNotificationView(generics.ListAPIView):
    serializer_class = NotificationsSerializers

    # queryset = Notifications.objects.filter(to_users=(request.user.profile,))
    def get_queryset(self):
        return Notifications.objects.filter(to_users=(self.request.user.profile.id,))


class AddSubscriptionForUser(generics.CreateAPIView):
    serializer_class = SubscriptionForUserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(watcher=self.request.user.profile)


class AddSubscriptionForCategory(generics.CreateAPIView):
    serializer_class = SubscriptionForCategorySerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(watcher=self.request.user.profile)


class AddSubscriptionForPost(generics.CreateAPIView):
    serializer_class = SubscriptionForPostSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(watcher=self.request.user.profile)
