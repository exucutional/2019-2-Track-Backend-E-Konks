from django.db import models
# Create your models here.

class Message(models.Model):
    chat = models.ForeignKey('chats.Chat', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    added_at = models.CharField(max_length=5 ,blank=True, null=True, default='00:00')
    content = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.content