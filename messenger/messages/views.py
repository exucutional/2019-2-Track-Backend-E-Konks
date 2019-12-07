from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import Http404
from messages.models import Message
from users.models import User
from messages.forms import MessagePostForm
from django.views.decorators.csrf import csrf_exempt
from django_eventstream import send_event
# Create your views here.

def message(request, message_id):
    if request.method == 'GET':
        try:
            message = Message.objects.get(id = message_id)
            user = User.objects.get(id = message.user_id)
            return JsonResponse({
                'id': message.id,
                'user_id': message.user_id,
                'username': user,
                'content': message.content,
            })
        except Message.DoesNotExist:
            raise Http404
        except User.DoesNotExist:
            raise Http404
    return HttpResponseNotAllowed(['GET'])

def messages_list(request):
    if request.method == 'GET':
        messages = list(Message.objects.values('id', 'chat_id', 'user_id', 'content'))
        try:
            for message in messages:
                user = User.objects.get(id = message['user_id'])
                message['username'] = str(user)
        except User.DoesNotExist:
            raise Http404
        response = JsonResponse({'messages': messages})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def message_create(request):
    if request.method == 'POST':
        form = MessagePostForm(request.POST)
        if form.is_valid():
            message = form.save()
            send_event('test', 'message', {'event': 'new message'})
            return JsonResponse({
                'msg': 'Сообщение сохранено',
                'id': message.id
            })
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])