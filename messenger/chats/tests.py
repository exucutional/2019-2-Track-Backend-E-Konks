from django.test import TestCase, Client
from selenium import webdriver
from users.models import User
from chats.models import Chat
from messages.models import Message
from chats.factory import RandomChatFactory 

# Create your tests here.

class SeleniumTests(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        self.driver.get("http://localhost:8000/login/")
        self.assertIn("Social Auth with Django", self.driver.title)
        elem = self.driver.find_element_by_link_text("Login with VK")
        self.assertIsNotNone(elem)
        elem = self.driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/button")
        self.assertIsNotNone(elem)
        elem.click()

    def test_index(self):
        self.driver.get("http://localhost:8000/")
        elem = self.driver.find_element_by_xpath("/html/body/h1[1]")
        self.assertIsNotNone(elem)

    def tearDown(self):
        self.driver.close()


class APITest(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")
        self.chat = RandomChatFactory.create()
        self.chat.save()
        message = Message(chat=self.chat, user=user, content='test')
        message.save()

    def test_chat_detail(self):
        response = self.client.get(f'/chats/{self.chat.id}/')
        self.assertEqual(response.status_code, 200)
        content = response.json()
        self.assertIsNotNone(content)

    def test_chat_list(self):
        response = self.client.get('/chats/list/')
        self.assertEqual(response.status_code, 200)
        content = response.json()
        self.assertIsNotNone(content)

    def test_chat_messages(self):
        response = self.client.get('/chats/1/messages/')
        self.assertEqual(response.status_code, 200)
        content = response.json()
        #print(content)

    def test_chat_create(self):
        response = self.client.post('/chats/create/', {
            'topic': 'test_chat_create',
        })
        self.assertEqual(response.status_code, 200)
        chat = Chat.objects.get(id=response.json()['id'])
