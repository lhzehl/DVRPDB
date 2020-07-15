from django_filters import rest_framework as filter

from .models import SubscriptionForUser
from users.models import Profile as Watcher


class SubscriptionForUserFilter(filter.FilterSet):

    author = filter.ModelChoiceFilter(
        watcher=Watcher.objects.all(), field_name='author', to_field_name='username'
    )

    class Meta:
        model = SubscriptionForUser
        fields = [
            'watcher'
        ]
