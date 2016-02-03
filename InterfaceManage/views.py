from django.core import serializers
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView
from InterfaceManage.models import ItProject
from InterfaceManage.utils import getResponse


class ProjectListView(ListView):

    pass

class ProjectDetailView(DetailView):
    model = ItProject

    def get(self, request, *args, **kwargs):
        id = request.GET['id']
        data = self.model.objects.all().filter(id=id)

        data = serializers.serialize('json', data)
        response_data = {}
        response_data['id'] = id
        response_data['data'] = data
        return getResponse(response_data)
