from django.urls import path
from messages.views import message
from messages.views import message_create
from messages.views import messages_list

urlpatterns = [
    path('<int:message_id>/', message, name='message'),
    path('list/', messages_list, name='messages_list'),
    path('create/', message_create, name='message_create'),
]

