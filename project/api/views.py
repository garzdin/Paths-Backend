from json import dumps
from django.core import serializers
from django.http import JsonResponse
from core.models import *

def index(request):
    return JsonResponse({"message": "Welcome to the API"})

def paths(request):
    return JsonResponse({"paths": [path.json() for path in Path.objects.all()]})
