from django.urls import path
from messages.views import message, message_create, messages_list
from messages.views import MessageViewSet
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register('DRF', MessageViewSet)

urlpatterns = [
    path('<int:message_id>/', message, name='message'),
    path('list/', messages_list, name='messages_list'),
    path('create/', message_create, name='message_create'),
]

urlpatterns += routers.urls
