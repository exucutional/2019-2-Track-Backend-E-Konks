from django import forms
from chats.models import Chat
from messages.models import Message

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['topic', 'last_message']

