from django.urls import path
from chats.views import index
from chats.views import chat_detail
from chats.views import chat_create
from chats.views import chat_list
from chats.views import chat_messages_list

urlpatterns = [
    path('<int:chat_id>/', chat_detail, name='chat_detail'),
    path('<int:chat_id>/messages/', chat_messages_list, name='chat_messages_list'),
    path('list/', chat_list, name='chat_list'),
    path('create/', chat_create, name='chat_create'),
]
