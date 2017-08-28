import json

from django.http import HttpResponse
from django.core import serializers

from profile_serializer import ProfileSerializer
from exchange.models import Language, Link, Profile

def index(request):
    return HttpResponse('qconvo')

def profiles(request):
    native = request.GET.get('n')
    learning = request.GET.get('l')
    profiles = Profile.objects.all().filter(
        nativelangs__name=native).filter(learninglangs__name=learning)
    s = ProfileSerializer()
    data = [s.serialize(p) for p in profiles]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type='application/json')

def languages(request):
    data = serializers.serialize('json', Language.objects.all())
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type = 'application/json')
