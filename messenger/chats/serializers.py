from rest_framework.serializers import ModelSerializer
from chats.models import Chat

class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = ['topic', 'last_message']
