from django.db import models

from users.models import Profile as User
from post.models import Post, Category


class Actions(models.Model):
    """
    This is all actions model, user create post/comment post/like post etc
    """
    by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=500)
    type = models.CharField('Type of instance', max_length=50)
    _id = models.PositiveIntegerField('Instance ID')

    def __str__(self):
        return f'{self.by_user.username} - {self.action}'


class Notifications(models.Model):
    """
    Notification model, connection with subscription model by signals
    """
    actions = models.OneToOneField(Actions, on_delete=models.CASCADE)
    to_users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.actions.by_user.username} - {self.actions.action}'


class SubscriptionForUser(models.Model):
    """
    This is model subscription  on user
    """
    watcher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='watch_for_user')
    object_of_observation = models.ForeignKey(User, on_delete=models.CASCADE, related_name='observation_for_user')

    def __str__(self):
        return f'{self.watcher.username} watch for {self.object_of_observation.username}'


class SubscriptionForPost(models.Model):
    """
    This is model subscription on post
    """
    watcher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='watch_for_post')
    object_of_observation = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='observation_for_post')

    def __str__(self):
        return f'{self.watcher.username} watch for {self.object_of_observation.title}'


class SubscriptionForCategory(models.Model):
    """
    This is model subscription on category
    """
    watcher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='watch_for_category')
    object_of_observation = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='observation_for_category')