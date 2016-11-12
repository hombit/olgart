from django.views.generic import DetailView

from paintings.models import Gallery, Painting


class GalleryDetailView(DetailView):
	model = Gallery

	def get_context_data(self, **kwargs):
		context = super(GalleryDetailView, self).get_context_data(**kwargs)
		context['paintings'] = Painting.objects.filter(gallery=self.get_object())
		return context


class PaintingDetailView(DetailView):
	model = Painting

	def get_context_data(self, **kwargs):
		context = super(PaintingDetailView, self).get_context_data(**kwargs)
		painting = context['object']
		paintings = Painting.objects.filter(gallery=painting.gallery).exclude(position=painting.position)
		context['previous_painting'] = paintings.order_by('-position').extra(where=['position < %s'], params=[painting.position]).first()
		context['next_painting'] = paintings.order_by('position').extra(where=['position > %s'], params=[painting.position]).first()
		return context
