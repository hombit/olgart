from django.views.generic import ListView

from exhibitions.models import Exhibition


class ExhibitionsListView(ListView):
	model = Exhibition
	def get_context_data(self, **kwargs):
		context = super(ExhibitionsListView, self).get_context_data(**kwargs)
		return context
