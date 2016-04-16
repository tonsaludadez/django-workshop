from django.shortcuts import render
from django.views.generic import DetailView

from myprojects.models import MyProject

class ProjectDetailView(DetailView):
	template_name = 'myprojects/detail.html'

	model = MyProject