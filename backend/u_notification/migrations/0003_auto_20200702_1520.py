# Generated by Django 3.0.3 on 2020-07-02 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('u_notification', '0002_auto_20200701_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actions',
            options={'verbose_name': 'Action', 'verbose_name_plural': 'Actions'},
        ),
        migrations.AlterModelOptions(
            name='notifications',
            options={'verbose_name': 'Notification', 'verbose_name_plural': 'Notifications'},
        ),
        migrations.AlterModelOptions(
            name='subscriptionforcategory',
            options={'verbose_name': 'subscription for category', 'verbose_name_plural': 'subscriptions for categories'},
        ),
        migrations.AlterModelOptions(
            name='subscriptionforpost',
            options={'verbose_name': 'subscription for post', 'verbose_name_plural': 'subscriptions for posts'},
        ),
        migrations.AlterModelOptions(
            name='subscriptionforuser',
            options={'verbose_name': 'subscription for user', 'verbose_name_plural': 'subscriptions for users'},
        ),
    ]