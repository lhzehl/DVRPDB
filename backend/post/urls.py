from django.urls import path
from .views import PostListView, CategoryListView, TagListView

urlpatterns =[
    path('posts/', PostListView.as_view()),
    path('tags/', TagListView.as_view()),
    path('categories/', CategoryListView.as_view())
]