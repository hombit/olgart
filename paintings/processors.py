from paintings.models import Gallery


def get_Galleries(request):
	return ( {'galleries' : Gallery.objects.all()} )
