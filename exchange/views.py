import json

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers

from user_serializer import UserSerializer
from exchange.models import Language

def index(request):
    return HttpResponse('qconvo')

def users(request):
    s = UserSerializer()
    data = [s.serialize(u) for u in User.objects.all()]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json')

def languages(request):
    data = serializers.serialize('json', Language.objects.all())
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type = 'application/json')
