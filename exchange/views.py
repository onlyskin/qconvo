import json

from django.http import HttpResponse

def users(request):
    response_data = {"message": "Hello World"}
    return HttpResponse(json.dumps(response_data),
                       content_type="application/json")
