from django_filters import rest_framework as filter

from .models import Post, Category, Tag
from users.models import Profile as Author


class PostFilter(filter.FilterSet):
    
    tags = filter.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(), field_name='tags__title', to_field_name='title'
    )
    category = filter.ModelChoiceFilter(
        queryset=Category.objects.all(), field_name='category', to_field_name='title'
    )

    author = filter.ModelChoiceFilter(
        queryset=Author.objects.all(), field_name='author', to_field_name='username'
    )

    class Meta:
        model = Post
        fields = [
            'tags', 'category', 'author'
        ]
