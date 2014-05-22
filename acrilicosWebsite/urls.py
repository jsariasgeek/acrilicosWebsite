from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.home', name='home'),
    url(r'^contacto/', 'website.views.contacto', name='contacto'),
    url(r'^proyectos/(?P<pk>\d+)/$', 'website.views.paginaProyecto', name='paginaProyecto'),
    url(r'^mensajeenviado/', 'website.views.gracias', name='gracias'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^website/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),

)
