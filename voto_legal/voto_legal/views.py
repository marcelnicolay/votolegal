import json

from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from voto_legal.models import Acompanhamento, Politico, PoliticoCategoriaProjeto


def home(request):
    facebook_profile = None
    if request.user.is_authenticated():
        facebook_profile = request.user.get_profile().get_facebook_profile()
    return render(request, 'home.html', {'facebook_profile': facebook_profile})


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


def ajax_politicos(request, nome):
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


def seguir_politico(request, slug):
    try:
        politico = Politico.objects.get(slug=slug)
    except Politico.DoesNotExist:
        raise Http404

    facebook_profile = request.user.get_profile().get_facebook_profile()
    politico.seguir(facebook_profile)
    context = {
        'status': 'ok',
    }

    return HttpResponse(json.dumps(context), mimetype='application/json')


def politicos_que_sigo(request):
    if not request.user.is_authenticated():
        raise Http404

    facebook_profile = request.user.get_profile().get_facebook_profile()
    politicos = []
    for acomp in Acompanhamento.objects.filter(user=facebook_profile).all():
        politico = acomp.politico
        politicos.append({
            'nome': politico.nome,
            'slug': politico.slug,
        })

    context = {
        'politicos': politicos,
    }

    return HttpResponse(json.dumps(context), mimetype='application/json')
