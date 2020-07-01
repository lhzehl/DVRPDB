from django.contrib import admin

from .models import StartMessage, ReplyMessage
# Register your models here.
admin.site.register(StartMessage)
admin.site.register(ReplyMessage)