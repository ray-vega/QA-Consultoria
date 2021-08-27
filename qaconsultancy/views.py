#Django
from django.http import HttpResponse, JsonResponse
import json
#Utilities
from datetime import datetime

def hello_world(request):
    
    return HttpResponse('Hello, world! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to QA Consultancy'.format(name)
    return HttpResponse(message)