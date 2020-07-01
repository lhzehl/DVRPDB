from rest_framework import generics
from .models import CustomUser, Profile
from .serializers import UserSerializer, ProfileSerializer


class UserView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer