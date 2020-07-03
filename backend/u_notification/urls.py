from django.urls import path
from .views import ActionsListView, UsersNotificationView


urlpatterns = [
    path('list/', ActionsListView.as_view()),
    path('notifications/', UsersNotificationView.as_view())
]