from channels.routing import ProtocolTypeRouter, URLRouter
from .channels_auth import UniversalAuthMiddlewareStack

from u_notification.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': UniversalAuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )

})