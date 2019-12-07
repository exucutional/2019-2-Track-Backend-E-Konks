from django import forms
from messages.models import Message

class MessagePostForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['chat', 'user', 'content']


