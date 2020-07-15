from django.urls import path
from .views import ActionsListView, UsersNotificationView,\
    AddSubscriptionForUser, AddSubscriptionForCategory, AddSubscriptionForPost, UsersSubList


urlpatterns = [
    path('list/', ActionsListView.as_view()),
    path('notifications/', UsersNotificationView.as_view()),
    path('watchuser/', AddSubscriptionForUser.as_view()),
    path('watchcategory/', AddSubscriptionForCategory.as_view()),
    path('watchpost/', AddSubscriptionForPost.as_view()),
    path('watchuserslist/', UsersSubList.as_view())

]