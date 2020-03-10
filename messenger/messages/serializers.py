from rest_framework.serializers import ModelSerializer
from messages.models import Message

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['chat', 'user', 'added_at', 'content']
