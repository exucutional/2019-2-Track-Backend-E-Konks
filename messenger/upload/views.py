from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse
from upload.forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def upload_file(request):
    pass
    '''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'response': 'ok'
            })
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])
    '''