from rest_framework import generics, permissions
# from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Tag, Category
from .serializers import PostSerializer, TagSerializer, CategorySerializer


class PostListView(generics.ListAPIView):
    """
    posts list
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

