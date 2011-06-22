from django.conf.urls.defaults import patterns, include, url
from livraria.models import Publicacao
from django.views.generic import DetailView, ListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ibd.views.home', name='home'),
    # url(r'^ibd/', include('ibd.foo.urls')),
    
    url(r'^livraria/', include('ibd.livraria.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',  'livraria.views.index'),
)
