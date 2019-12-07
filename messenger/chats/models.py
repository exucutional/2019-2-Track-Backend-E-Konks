from django.db import models

# Create your models here.
class Chat(models.Model):
    topic = models.CharField(max_length=32, null=False, verbose_name='Название')
    last_message = models.ForeignKey(
        'chat_messages.Message', 
        related_name='messages_chats',
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        verbose_name='Последнее сообщение'
        )

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return self.topic


class Member(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey('Chat', on_delete=models.SET_NULL, null=True)
    last_read_message = models.ForeignKey('chat_messages.Message', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Член'
        verbose_name_plural = 'Члены'

    def __str__(self):
        return self.user.username


class Attachment(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    message = models.ForeignKey('chat_messages.Message', on_delete=models.SET_NULL, null=True)
    attype = models.CharField(max_length=32, null=False, verbose_name='Type')
    url = models.URLField(null=False, verbose_name='URL')
