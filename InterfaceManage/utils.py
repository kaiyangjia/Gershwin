import json
from django.http import HttpResponse

__author__ = 'jia'


content_type="application/json"
def getResponse(response_data):
    return HttpResponse(json.dumps(response_data, ensure_ascii=False), content_type=content_type)