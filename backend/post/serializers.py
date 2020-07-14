from rest_framework import serializers

from .models import Post, Comments, Category, Tag
from users.models import Profile as Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    post/comment author
    """

    class Meta:
        model = Author
        fields = [
            'id', 'username', 'image'
        ]


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'title'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentsListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Comments
        fields = [
            'author', 'id', 'date_add', 'text'
        ]


class PostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategoryListSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'author',
            'id', 'title', 'image',
            'descriptions', 'date_create',
            'category', 'tags'
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategoryListSerializer()
    tags = TagSerializer(many=True)
    comments = CommentsListSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = [
            'author',
            'id', 'title', 'image',
            'descriptions', 'date_create',
            'category', 'tags', 'comments'
        ]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title', 'image', 'descriptions',
            'category', 'tags', 'id'
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['post', 'text']


class CommentUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'text'
        ]
