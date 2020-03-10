from django.urls import path
from rest_framework import routers
from chats.views import index, chat_detail, chat_create, chat_list, chat_messages_list
from chats.views import ChatViewSet


router = routers.DefaultRouter()
router.register('DRF', ChatViewSet)

urlpatterns = [
    path('<int:chat_id>/', chat_detail, name='chat_detail'),
    path('<int:chat_id>/messages/', chat_messages_list, name='chat_messages_list'),
    path('list/', chat_list, name='chat_list'),
    path('create/', chat_create, name='chat_create'),
]

urlpatterns += router.urls