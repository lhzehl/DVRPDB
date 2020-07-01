from django.urls import path

from .views import StartMessageView, ReplyMessageView, RDialogListView, SDialogListView, DialogDetailView

urlpatterns = [
    path('start/', StartMessageView.as_view()),
    path('reply/', ReplyMessageView.as_view()),
    path('slist/', SDialogListView.as_view()),
    path('rlist/', RDialogListView.as_view()),
    path('<int:pk>/', DialogDetailView.as_view())

]
