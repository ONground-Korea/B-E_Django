from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    if request.method == "GET":
       return JsonResponse({'req_method':'get'})

    elif request.method == "POST":
        return JsonResponse({'req_method':'post'})

    else:
        return JsonResponse({'error': 'request method not allowed'}, status = 405)
