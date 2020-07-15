from django.urls import path

from .consumers import NotificationUserConsumer

websocket_urlpatterns = [
    path('notification/', NotificationUserConsumer)
]