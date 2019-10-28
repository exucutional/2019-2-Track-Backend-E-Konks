from django.urls import path
from chats.views import index
from chats.views import chat_detail

urlpatterns = [
    path('index/', index, name='index'),
    path('<int:chat_id>/', chat_detail, name='chat_detail'),
]
