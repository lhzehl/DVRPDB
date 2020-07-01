from django.apps import AppConfig


class UNotificationConfig(AppConfig):
    name = 'u_notification'

    def ready(self):
        import u_notification.signals
