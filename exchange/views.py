import json

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers

from user_serializer import UserSerializer
from exchange.models import Language
from exchange.models import Link

def index(request):
    return HttpResponse('qconvo')

def users(request, native, learning):
    links = Link.objects.all().filter(level='n').filter(language__name=native);
    users = map(lambda x: x.profile.user, links)
    s = UserSerializer()
    data = [s.serialize(u) for u in users]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json')

def languages(request):
    data = serializers.serialize('json', Language.objects.all())
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type = 'application/json')
