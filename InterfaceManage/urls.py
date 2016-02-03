from django.conf.urls import url
from InterfaceManage.views import ProjectListView, ProjectDetailView

__author__ = 'jia'

urlpatterns = [
    url(r'/project/list/*', ProjectListView.as_view(), name='project_list'),
    url(r'/project/*', ProjectDetailView.as_view(), name='project_detail'),
]