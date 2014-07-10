from django.views.generic import DetailView, ListView

from paintings.models import Gallery, Painting


class GalleryDetailView(DetailView):
	model = Gallery
	slug_field = 'title_en'

	def get_context_data(self, **kwargs):
		context = super(GalleryDetailView, self).get_context_data(**kwargs)
		context['paintings'] = Painting.objects.filter(gallery=self.get_object())
		#print(gallery)
		return context


class GalleryListView(ListView):
	model = Gallery


class PaintingDetailView(DetailView):
	model = Painting
