from random import randrange

from paintings.models import Gallery, Painting


def get_Galleries(request):
	return ( {'galleries' : Gallery.objects.all()} )


def get_random_canvasOilPainting(request):
	paintings = Painting.objects.filter(surface='canvas', material='oil').extra(where=['width > height'])
	rand_painting = paintings[ randrange( paintings.__len__() ) ]
	return ( {'rand_painting' : rand_painting} )
