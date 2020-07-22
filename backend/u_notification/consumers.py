from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import login

import json


class NotificationUserConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope['user']
        # self.group_name = self.user.profile.username
        self.group_name='test'


        print(self.user, self.group_name)

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

    async def receive(self, text_data):
        ...
        # login the user to this session.
        await login(self.scope, user)
        # save the session (if the session backend does not access the db you can use `sync_to_async`)
        await database_sync_to_async(self.scope["session"].save)()
