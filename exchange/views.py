import json

from django.http import HttpResponse
from django.core import serializers
from django.template.loader import render_to_string

from profile_serializer import ProfileSerializer
from exchange.models import Language, Link, Profile

def tests(request):
    rendered = render_to_string('tests.html')
    return HttpResponse(rendered)

def index(request):
    rendered = render_to_string('exchange.html')
    return HttpResponse(rendered)

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
    data = [language.name for language in Language.objects.all()]
    response_data = json.dumps(data)
    return HttpResponse(response_data, content_type = 'application/json')
