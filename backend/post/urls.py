from django.urls import path
from .views import PostListView, CategoryListView, TagListView,\
    PostDetailView, PostCreateView, CommentCreateView,\
    CategoryCreateView, TagCreateView, CommentUpdateDeleteView

urlpatterns =[
    path('posts/', PostListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('newpost/', PostCreateView.as_view()),
    path('comment/<int:pk>/', CommentUpdateDeleteView.as_view()),
    path('newcomment/', CommentCreateView.as_view()),
    path('tags/', TagListView.as_view()),
    path('newtag/', TagCreateView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('newcategory/', CategoryCreateView.as_view()),
]