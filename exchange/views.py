from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers

def index(request):
    return HttpResponse('qconvo')

def users(request):
    response_data = serializers.serialize('json', User.objects.all(),
        fields=('username', 'languages'))
    return HttpResponse(response_data,
                       content_type='application/json')
