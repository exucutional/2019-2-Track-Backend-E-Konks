from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import Http404
# Create your views here.

def message(request):
    if request.method == 'GET':
        message_id = request.GET.get('id')
    else:
        return HttpResponseNotAllowed(request.method)
    return JsonResponse({'id': message_id, 'name': 'Name', 'time': '00:00', 'message': 'Message'})