from django.db import models
from django.utils.timezone import now
# Create your models here.

class Message(models.Model):
    chat = models.ForeignKey('chats.Chat', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    added_at = models.TimeField(verbose_name='Время создания', default=now)
    content = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.content
