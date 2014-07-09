from django.views.generic import DetailView, ListView

from paintings.models import Painting


class PaintingDetailView(DetailView):
	model = Painting


class PaintingsListView(ListView):
	model = Painting
