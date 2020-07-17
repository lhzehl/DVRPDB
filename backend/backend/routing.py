  
from channels.routing import ProtocolTypeRouter, URLRouter

# from channels.auth import AuthMiddlewareStack
from u_notification.routing import websocket_urlpatterns
from u_notification.token_auth import TokenAuthMiddlewareStack

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': TokenAuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )

})