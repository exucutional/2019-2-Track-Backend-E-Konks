from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import Http404
from messages.models import Message
from users.models import User
from messages.forms import MessagePostForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django_eventstream import send_event
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messages.serializers import MessageSerializer
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60)
@login_required
def message(request, message_id):
    if request.method == 'GET':
        try:
            message = Message.objects.get(id = message_id)
            user = User.objects.get(id = message.user_id)
            return JsonResponse({
                'id': message.id,
                'user_id': message.user_id,
                'username': user.username,
                'content': message.content,
            })
        except Message.DoesNotExist:
            raise Http404
        except User.DoesNotExist:
            raise Http404
    return HttpResponseNotAllowed(['GET'])

@login_required
def messages_list(request):
    if request.method == 'GET':
        messages = list(Message.objects.values('id', 'chat_id', 'user_id', 'added_at', 'content'))
        try:
            for message in messages:
                user = User.objects.get(id = message['user_id'])
                message['username'] = str(user)
        except User.DoesNotExist:
            raise Http404
        response = JsonResponse({'messages': messages})
        return response
    return HttpResponseNotAllowed(['GET'])


def send_new_message_event():
    send_event('test', 'message', {'event': 'new message'})

@login_required
@csrf_protect
def message_create(request):
    if request.method == 'POST':
        form = MessagePostForm(request.POST)
        if form.is_valid():
            message = form.save()
            send_new_message_event()
            return JsonResponse({
                'msg': 'Сообщение сохранено',
                'id': message.id
            })
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
