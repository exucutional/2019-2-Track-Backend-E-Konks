from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import Http404
# Create your views here.

def user_contacts(request):
    if request.method == 'GET':
        user_id = request.GET.get('id')
    else:
        return HttpResponseNotAllowed(request.method)
    return JsonResponse({'id': user_id, 'contacts': 'null'})


def user_detail(request):
    if request.method == 'GET':
        user_id = request.GET.get('id')
    else:
        return HttpResponseNotAllowed(request.method)
    return JsonResponse({'id': user_id, 'fname': 'FirstName', 'sname': 'SecondName', 'detail': 'null'})
