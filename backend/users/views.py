from rest_framework import generics, permissions
from .models import CustomUser, Profile
from .serializers import UserSerializer, ProfileSerializer
from .custom_permissions import IsCurrentUserOrAdmin


class UserView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsCurrentUserOrAdmin]
