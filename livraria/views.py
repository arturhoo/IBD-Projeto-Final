from django.shortcuts import render_to_response
from django.http import Http404
from livraria.models import Publicacao

def index(request):
    latest_pub_list = Publicacao.objects.all().order_by('-data_lancamento')[:5]
    return render_to_response('livraria/index.html', {'latest_pub_list' : latest_pub_list})

def titleSearch(request, title):
    try:
        p = Publicacao.objects.filter(titulo__icontains=title)
    except Publicacao.DoesNotExist:
        raise Http404
    return render_to_response('livraria/search.html', {'pubs': p, 'searchkey':title})

def authorSearch(request, name):
    try:
        p = Publicacao.objects.filter(autores__nome__icontains=name)
    except Publicacao.DoesNotExist:
        raise Http404
    return render_to_response('livraria/search.html', {'pubs': p,
        'searchkey':name})

def detail(request, pub_id):
    try:
        p = Publicacao.objects.get(pk=pub_id)
    except Publicacao.DoesNotExist:
        raise Http404
    return render_to_response('livraria/detail.html', {'pub': p})
