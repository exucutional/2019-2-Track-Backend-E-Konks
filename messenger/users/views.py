from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import Http404
from users.models import User
from messages.models import Message
# Create your views here.

def user_detail(request, user_id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=user_id)
            response = JsonResponse({
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'email': user.email,
                'bio': user.bio
            })
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            return response
        except User.DoesNotExist:
            raise Http404
    return HttpResponseNotAllowed(['GET'])


def user_search(request):
    if request.method == 'GET':
        users = User.objects.filter(username__contains=request.GET.get('username'))
        return JsonResponse({
            'data': list(users.values('id', 'first_name', 'last_name', 'username'))
        })
