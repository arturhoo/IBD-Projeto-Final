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

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 
        ListView.as_view(
            queryset=Publicacao.objects.order_by('-data_lancamento')[:5],
            context_object_name='latest_pub_list',
            template_name='livraria/index.html')),
)
