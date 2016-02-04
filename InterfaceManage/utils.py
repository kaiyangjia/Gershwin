# coding=utf-8
import json
from django.core import serializers
from django.http import HttpResponse

__author__ = 'jia'


content_type="application/json"
def getResponse(response_data):
    return HttpResponse(json.dumps(response_data, ensure_ascii=False), content_type=content_type)

def getErrorParamsResponse():
    response_data = {}
    response_data['code'] = -1
    response_data['msg'] = 'param error'
    return response_data

def getJson(queryset):
    data = json.loads(serializers.serialize('json', queryset))
    result = []
    for e in data:
        result.append(e['fields'])
    return result