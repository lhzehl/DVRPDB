from django.db.models.signals import post_save
from django.dispatch import receiver

from post.models import Post, Comments
# from users.models import Profile

from .models import Actions, Notifications, SubscriptionForUser, SubscriptionForPost, SubscriptionForCategory


@receiver(post_save, sender=Comments)
def new_comment_listeners(sender, instance, created, **kwargs):
    """
    create notification when someone comment post
    :param created: only if new comment (not edited)
    :param sender: The model class that just had an instance created. ( Comments)
    :param instance: object of Comments
    :param kwargs:
    :return:
    """
    if created:
        message = f'comment post {instance.post.title}'
        action = Actions(by_user=instance.author, action=message, type='comment', _id=instance.id)
        action.save()

        notification = Notifications(actions=action)
        notification.save()

        # Check for subscription on user
        subscriptions_on_user = SubscriptionForUser.objects.filter(object_of_observation=instance.author)

        for sub in subscriptions_on_user:
            watcher = sub.watcher
            if not watcher == instance.author:
                watcher.new_notification += 1
                notification.to_users.add(watcher)

        # Check for subscription on post
        subscriptions_on_post = SubscriptionForPost.objects.filter(object_of_observation=instance.post)

        for sub in subscriptions_on_post:
            watcher = sub.watcher
            if not watcher == instance.author:
                watcher.new_notification += 1
                notification.to_users.add(watcher)

        if not instance.author == instance.post.author:
            instance.author.new_notification += 1
            notification.to_users.add(instance.post.author)


@receiver(post_save, sender=Post)
def new_post_listener(sender, instance, created, **kwargs):
    """
    create notification when someone create post
    :param sender: only if new post (not edited)
    :param instance: The model class that just had an instance created. ( Post)
    :param created: object of Post
    :param kwargs:
    :return:
    """
    if created:
        message = f'add new post - {instance.title}'
        action = Actions(by_user=instance.author, action=message, type='post', _id=instance.id)
        action.save()

        notification = Notifications(actions=action)
        notification.save()

        # Check for subscription on user
        subscriptions_on_user = SubscriptionForUser.objects.filter(object_of_observation=instance.author)

        for sub in subscriptions_on_user:
            watcher = sub.watcher
            notification.to_users.add(watcher)

        # Check for subscription on category
        subscriptions_on_category = SubscriptionForCategory.objects.filter(object_of_observation=instance.category)

        for sub in subscriptions_on_category:
            watcher = sub.watcher
            if not watcher == instance.author:
                notification.to_users.add(watcher)

        for user in notification.to_users.all():
            user.new_notification += 1
            user.save()
