import factory
from messages.models import Message
from chats.models import Chat
from users.models import User

class RandomMessageFactory(factory.Factory):
    class Meta: 
        model = Message

    chat = Chat.objects.get(id=1)
    user = User.objects.get(id=1)
    content = factory.Faker('text')
