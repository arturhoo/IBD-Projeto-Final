# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from livraria.models import Publicacao
from django import forms

MY_CHOICES = (
    ('autor', 'Nome do Autor'),
    ('titulo', 'Título da Publicação')
)

class SearchForm(forms.Form):
    value = forms.CharField(label="Palavra-chave", max_length=100)
    stype = forms.ChoiceField(label="Pesquisar por",choices=MY_CHOICES)

def index(request):
    f = SearchForm()
    latest_pub_list = Publicacao.objects.all().order_by('-data_lancamento')[:5]
    c = RequestContext(request, {
        'latest_pub_list': latest_pub_list,
        'form': f,
    })
    return render_to_response('livraria/index.html', c)

def search(request):
    if request.method == 'POST':
        f = SearchForm(request.POST) # A form bound to the POST data
        if f.is_valid(): # All validation rules pass
            value = f.cleaned_data['value']
            stype = f.cleaned_data['stype']
            if (stype == 'autor'):
                p = Publicacao.objects.filter(autores__nome__icontains=value)
                c = RequestContext(request, {
                    'pubs': p, 
                    'searchkey': value,
                    'form': f,
                })
                return render_to_response('livraria/index.html', c)
            else:
                p = Publicacao.objects.filter(titulo__icontains=value)
                c = RequestContext(request, {
                    'pubs': p, 
                    'searchkey': value,
                    'form': f,
                })
                return render_to_response('livraria/index.html', c)
        else:
            return index(request)
    else:
        return index(request)



def detail(request, pub_id):
    try:
        p = Publicacao.objects.get(pk=pub_id)
    except Publicacao.DoesNotExist:
        raise Http404
    return render_to_response('livraria/detail.html', {'pub': p})
