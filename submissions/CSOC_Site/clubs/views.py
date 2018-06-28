from django.views.generic import TemplateView
from .models  import clubs

class IndexView(TemplateView):
	template_name = 'clubs/clubs.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		club = clubs.objects.all()
		context = {'club':club}
		return context
