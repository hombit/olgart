from django.views.generic import ListView

from exhibitions.models import Exhibition


class ExhibitionsListView(ListView):
	model = Exhibition
