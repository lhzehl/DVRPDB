from django.urls import path
from .views import UserView, ProfileView


urlpatterns = [
    path('user/<int:pk>/', UserView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view())
]