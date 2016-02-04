import json
from django.core import serializers

# Create your views here.
from django.views.generic import ListView, DetailView
from InterfaceManage.models import ItProject, ItRelaUserProject
from InterfaceManage.utils import getResponse, getErrorParamsResponse, getJson


class ProjectListView(ListView):
    model = ItProject

    def get(self, request, *args, **kwargs):
        user_id = -1
        if request.GET.has_key('user_id'):
            user_id = request.GET['user_id']
        else:
            return getResponse(getErrorParamsResponse())

        data = {}
        response_data = {}
        data_join = []
        data_create = []
        if user_id != -1:
            q = ItRelaUserProject.objects.all().filter(user_id=user_id)
            data_create = getJson(self.model.objects.filter(create_user=user_id))
            for e in q:
                data_row = getJson(self.model.objects.all().filter(id=e.project_id))
                data_join.append(data_row)

        data['join'] = data_join
        data['create'] = data_create
        response_data['user_id'] = user_id
        response_data['code'] = 0
        response_data['data'] = data

        return getResponse(response_data)

class ProjectDetailView(DetailView):
    model = ItProject

    def get(self, request, *args, **kwargs):
        id = create_user = -1
        if request.GET.has_key('id'):
            id = request.GET['id']
        if request.GET.has_key('create_user'):
            create_user = request.GET['create_user']

        data = {}
        response_data = {}
        if id != -1:
            data = getJson(self.model.objects.all().filter(id=id))
            response_data['id'] = id
        elif create_user != -1:
            data = getJson(self.model.objects.all().filter(create_user=create_user))
            response_data['create_user'] = create_user
        response_data['data'] = data
        return getResponse(response_data)
