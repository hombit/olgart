from django.conf.urls import patterns, url
from django.contrib import admin

from exhibitions.views import ExhibitionsListView


admin.autodiscover()


urlpatterns = patterns('',
	url( r'^$', ExhibitionsListView.as_view(), name='exhibitions' ),
)
