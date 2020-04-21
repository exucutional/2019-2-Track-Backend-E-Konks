from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseNotFound
from django.http import Http404
from users.models import User
from messages.models import Message
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@cache_page(60)
@login_required
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
            return response
        except User.DoesNotExist:
            raise Http404
    return HttpResponseNotAllowed(['GET'])

@cache_page(60)
def user_search(request):
    if request.method == 'GET':
        users = User.objects.filter(username__contains=request.GET.get('username'))
        return JsonResponse({
            'data': list(users.values('id', 'first_name', 'last_name', 'username'))
        })

    return HttpResponseNotAllowed(['GET'])



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
