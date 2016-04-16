from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import TemplateView

from myprofile.models import MyProfile

from myprojects.models import MyProject

def home(request):
	me = MyProfile.objects.last()
	
	return HttpResponse("Hello world, I am " + me.full_name)

class HomepageView(TemplateView):
	template_name = 'myprofile/home.html'

	def get_context_data(self):
		context = super(HomepageView, self).get_context_data()
		context['me'] = MyProfile.objects.last()
		context['projects'] = MyProject.objects.all()

		return context
