from django_filters import rest_framework as filter

from .models import Post, Category, Tag
from users.models import Profile as Author


class PostFilter(filter.FilterSet):
    
    tags = filter.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(), to_field_name='title'
    )
    category = filter.ModelChoiceFilter(
        queryset=Category.objects.all(), to_field_name='title'
    )
    author = filter.ModelChoiceFilter(
        queryset=Author.objects.all(), to_field_name='username'
    )

    class Meta:
        model = Post
        fields = [
            'tags', 'category', 'author'
        ]
