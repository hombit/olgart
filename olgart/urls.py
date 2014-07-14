from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$', 'olgart.views.index', name='index'),
	url(r'^feedback/', 'olgart.views.feedback', name='feedback'),
	
	url( r'^exhibitions/', include('exhibitions.urls') ),
	url( r'^galleries/', include('paintings.urls') ),

    url( r'^admin/', include(admin.site.urls) ),
)
