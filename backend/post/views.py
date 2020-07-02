from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Tag, Category, Comments

from .serializers import PostListSerializer, TagSerializer, CategoryListSerializer, \
    PostDetailSerializer, PostCreateSerializer, CommentCreateSerializer, \
    CommentUpdateDeleteSerializer, CategorySerializer

from .custom_filter import PostFilter

from .custom_permissions import IsAuthorOrStaffOrReadOnlyPermission


class PostListView(generics.ListAPIView):
    """
    ### posts list
    """
    serializer_class = PostListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter
    queryset = Post.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    ### Post detail
    """
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthorOrStaffOrReadOnlyPermission]


class PostCreateView(generics.CreateAPIView):
    """
    ### create post
    """
    serializer_class = PostCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)


class CommentCreateView(generics.CreateAPIView):
    """
    ### create comment
    """
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)


class CommentUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    ### update and delete comment
    """
    serializer_class = CommentUpdateDeleteSerializer
    queryset = Comments.objects.all()
    permission_classes = [IsAuthorOrStaffOrReadOnlyPermission]


class TagListView(generics.ListAPIView):
    """
    ### tags list
    """
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagCreateView(generics.CreateAPIView):
    """
    ### create tag
    """
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryListView(generics.ListAPIView):
    """
    ### Categories list
    """
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryCreateView(generics.CreateAPIView):
    """
    ### create category
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
