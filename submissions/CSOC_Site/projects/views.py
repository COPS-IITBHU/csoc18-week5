from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Information


class IndexView(TemplateView):
	template_name = 'projects/projects.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class TeamView(TemplateView):
	template_name = 'projects/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		team_name = kwargs.get('team_name')
		team = get_object_or_404(Information, team_name=team_name)
		context['info'] = team.team_info
		context['name'] = team_name
		context['image'] = team.image_name
		return context
