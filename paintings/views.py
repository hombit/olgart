from django.views.generic import DetailView, ListView

from paintings.models import Gallery, Painting


class GalleryListView(ListView):
	model = Gallery


class PaintingDetailView(DetailView):
	model = Painting


class PaintingsListView(ListView):
	model = Painting
