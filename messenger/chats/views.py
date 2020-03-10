from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import Http404
from django import forms
from chats.models import Chat
from chats.forms import ChatForm
from messages.models import Message
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from users.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from chats.serializers import ChatSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    return HttpResponseNotAllowed(['GET'])


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html') 


@login_required
def chat_detail(request, chat_id):
    if request.method == 'GET':
        try:
            chat = Chat.objects.get(id=chat_id)
            return JsonResponse({
                    'topic': chat.topic,
                    'last_message_id': chat.last_message_id
                })
        except Chat.DoesNotExist:
            raise Http404
    return HttpResponseNotAllowed(['GET'])


@login_required
def chat_list(request):
    if request.method == 'GET':
        chats = Chat.objects.all().values('id', 'topic')
        return JsonResponse({'chats': list(chats)})
    return HttpResponseNotAllowed(['GET'])


@login_required
def chat_messages_list(request, chat_id):
    if request.method == 'GET':
        messages = Message.objects.filter(chat_id=chat_id)
        messages_list = list(messages.values('id', 'user_id', 'content'))
        return JsonResponse({'messages': messages_list})
    return HttpResponseNotAllowed(['GET'])


@login_required
@csrf_exempt
def chat_create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save()
            return JsonResponse({
                'msg': 'Пост сохранен',
                'id': chat.id
            })
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])


class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
