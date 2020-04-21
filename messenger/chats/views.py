from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import Http404
from django import forms
from chats.models import Chat
from chats.models import Member
from chats.forms import ChatForm
from messages.models import Message
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from users.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from chats.serializers import ChatSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from chats.forms import FormWithCaptcha
from chats.tasks import send_email
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    return HttpResponseNotAllowed(['GET'])


def login(request):
    form = FormWithCaptcha()
    return render(request, 'login.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html') 


@cache_page(60)
@csrf_protect
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


@cache_page(60)
def chat_list(request):
    if request.method == 'GET':
        chats = []
        for chat in Chat.objects.all():
            resp_chat = {
                'id': chat.id,
                'name': chat.topic,
            }
            if chat.last_message:
                resp_chat['time'] = chat.last_message.added_at
                resp_chat['message'] = chat.last_message.content
            chats.append(resp_chat)

        return JsonResponse({'chats': list(chats)})
    return HttpResponseNotAllowed(['GET'])


@cache_page(60)
@login_required
def chat_messages_list(request, chat_id):
    if request.method == 'GET':
        messages = Message.objects.filter(chat_id=chat_id)
        messages_list = list(messages.values('id', 'user_id', 'content'))
        return JsonResponse({'messages': messages_list})
    return HttpResponseNotAllowed(['GET'])

@login_required
@csrf_protect
def chat_create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save()
            return JsonResponse({
                'msg': 'Чат сохранен',
                'id': chat.id
            })
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])

@csrf_protect
def chat_personal_create(request):
    if request.method == 'POST':
        chatForm = ChatForm(request.POST)
        if chatForm.is_valid():
            try:
                user1 = User.objects.get(id=request.POST['user1'])
                user2 = User.objects.get(id=request.POST['user2'])
                chat = chatForm.save()
                member1 = Member(chat=chat, user=user1)
                member2 = Member(chat=chat, user=user2)
                member1.save()
                member2.save()
                send_email.delay([user1.email, user2.email])
                return JsonResponse({
                    'msg': 'Чат сохранен',
                    'id': chat.id
                })
            except User.DoesNotExist:
                raise Http404
        return JsonResponse({'errors': chatForm.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])

class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
