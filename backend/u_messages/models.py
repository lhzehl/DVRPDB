from django.db import models
from users.models import Profile as User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Dialog(models.Model):
    sender = models.ForeignKey(User, verbose_name='Author', related_name='sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, verbose_name='Listener', related_name='recipient', on_delete=models.CASCADE)
    message = models.TextField('Message')
    date_send = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField('Read', default=False)

    def __str__(self):
        return f'{self.sender} - {self.recipient} - id:{self.id}'


class Reply(models.Model):
    sender = models.ForeignKey(User, verbose_name='Answerer', on_delete=models.CASCADE)
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE, verbose_name='Dialog', related_name="reply")
    message = models.TextField('Message')
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}  - message_id:{self.id} - dialog_id:{self.dialog.id}'
