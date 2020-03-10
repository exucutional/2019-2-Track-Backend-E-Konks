from django.test import TestCase, Client
from users.models import User
from chats.factory import RandomChatFactory
from messages.factory import RandomMessageFactory

# Create your tests here.

class APITest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")
        self.chat = RandomChatFactory.build()
        self.chat.save()
        self.message = RandomMessageFactory.build(chat=self.chat, user=self.user)
        self.message.save()

    def test_user(self):
        response = self.client.get(f'/users/{self.user.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['username'], self.user.username)

    def test_user_search(self):
        response = self.client.get(f'/users/search/?username={self.user.username}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data'][0]['username'], self.user.username)
