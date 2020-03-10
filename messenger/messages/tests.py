import factory
from unittest.mock import patch
from django.test import TestCase, Client
from chats.factory import RandomChatFactory
from messages.factory import RandomMessageFactory
from users.factory import RandomUserFactory
from users.models import User

# Create your tests here.

class MessageClassTest(TestCase):

    def setUp(self):
        self.chat = RandomChatFactory.build()
        self.chat.save()
        self.user = RandomUserFactory.build()
        self.user.save()
        self.message = RandomMessageFactory()

    def test_str(self):
        self.assertEqual(self.message.content, str(self.message))

class APITest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")
        self.chat = RandomChatFactory.build()
        self.chat.save()
        self.message = RandomMessageFactory.build(chat=self.chat, user=self.user)
        self.message.save()

    def test_message(self):
        response = self.client.get(f'/messages/{self.message.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['username'], self.user.username)

    def test_messages_list(self):
        response = self.client.get('/messages/list/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()['messages']), 0)

    @patch('messages.views.send_new_message_event')
    def test_message_create(self, send_new_message_event_mock):
        response = self.client.post('/messages/create/', {
            'chat': self.chat.id,
            'user': self.user.id,
            'content': factory.Faker('text'),
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], self.message.id + 1)
        self.assertTrue(send_new_message_event_mock.called)
