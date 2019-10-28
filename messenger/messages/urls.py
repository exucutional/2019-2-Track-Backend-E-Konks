from django.urls import path
from messages.views import message

urlpatterns = [
    path('', message, name='message'),
]

