from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView


class ProjectListView(ListView):

    pass

class ProjectDetailView(DetailView):

    def get(self, request, *args, **kwargs):
        pass
