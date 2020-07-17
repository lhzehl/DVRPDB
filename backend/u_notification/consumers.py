from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import login
import json


class NotificationUserConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # await login(self.scope, user)
        # user = self.scope["user"]

        self.group_name = 'notifications'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )


    async def send_message(self, event):
        message = event['text']

        # Send message to WebSocket
        await self.send(text_data=json.dumps(
            message
        ))