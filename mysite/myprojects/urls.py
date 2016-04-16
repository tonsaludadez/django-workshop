from django.conf.urls import url
from django.contrib import admin

from myprojects import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
]
