from django.conf.urls import url
from django.contrib import admin

from myprofile import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^new-home/$', views.HomepageView.as_view()),
]
