from django.conf.urls.defaults import *
from livraria.models import Publicacao
from django.views.generic import DetailView, ListView

urlpatterns = patterns('livraria.views',
    (r'^$', 'index'),
#        ListView.as_view(
#            queryset=Publicacao.objects.order_by('-data_lancamento')[:5],
#            context_object_name='latest_pub_list',
#            template_name='livraria/index.html')),
    (r'^pub/(?P<pub_id>\d+)/$', 'detail'),
    (r'^search/$', 'search'),
    (r'^tsearch/(?P<title>[^/]+)/$', 'titleSearch'),
    (r'^asearch/(?P<name>[^/]+)/$', 'authorSearch'),
)
