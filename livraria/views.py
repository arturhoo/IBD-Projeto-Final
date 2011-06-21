from django.shortcuts import render_to_response
from livraria.models import Publicacao

def index(request):
    latest_pub_list = Publicacao.objects.all().order_by('-data_lancamento')[:5]
    return render_to_response('livraria/index.html', {'latest_pub_list' : latest_pub_list})
