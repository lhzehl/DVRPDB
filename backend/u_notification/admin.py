from django.contrib import admin
from .models import Actions, Notifications, SubscriptionForUser, SubscriptionForPost, SubscriptionForCategory

admin.site.register(Actions)
admin.site.register(Notifications)
admin.site.register(SubscriptionForUser)
admin.site.register(SubscriptionForPost)
admin.site.register(SubscriptionForCategory)
