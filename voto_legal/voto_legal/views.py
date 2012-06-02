import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from voto_legal.models import Politico, PoliticoCategoriaProjeto


def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def politico_view(request, slug):
    politico = get_object_or_404(Politico, slug=slug)
    categorias = PoliticoCategoriaProjeto.objects.filter(politico=politico)
    
    total_relevantes = 0
    total_irrelevantes = 0
    
    for categoria in categorias:
        if categoria.categoria_projeto.relevante:
            total_relevantes += categoria.quantidade
        else:
            total_irrelevantes += categoria.quantidade
        
    return render(request, 'politico.html', {
        'politico': politico,
        'categorias': categorias,
        'total_relevantes': total_relevantes,
        'total_irrelevantes': total_irrelevantes
    })


def archive_politicos(request):
    return render(request, 'archive-politico.html')


def search_politico(request):
    nome = request.GET.get('q', '')
    politicos = (Politico.objects.filter(Q(apelido__icontains=nome) | Q(nome__icontains=nome))
            .order_by('apelido', 'nome')[:20])
    context = {}
    if politicos:
        context['politicos'] = []
        for p in politicos:
            context['politicos'].append({
                'label': p.apelido,
                'value': p.slug,
            })
    else:
        context['politicos'] = None

    return HttpResponse(json.dumps(context), mimetype='application/json')


def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)
