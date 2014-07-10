from django.conf.urls import patterns, include, url
from django.contrib import admin

from paintings.views import GalleryDetailView, PaintingDetailView

admin.autodiscover()


urlpatterns = patterns('',
	url( r'^(?P<slug>\w+)/$', GalleryDetailView.as_view(), name='gallery' ),
	url( r'^(?P<gallery>\w+)/(?P<pk>\d+)/$', PaintingDetailView.as_view() ),
)
