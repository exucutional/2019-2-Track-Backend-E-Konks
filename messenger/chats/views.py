from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import Http404
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponseNotAllowed(request.method)
            


def chat_detail(request, chat_id):
    if request.method == 'GET':
        #chat_id = request.GET.get('id')
        
    else:
        return HttpResponseNotAllowed(request.method)
    return JsonResponse({'id': chat_id, 'name': 'Name', 'messages': 'null'})
    #return render(request, 'index.html')
