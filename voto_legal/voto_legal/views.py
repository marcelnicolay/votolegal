import json

from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from voto_legal.models import Acompanhamento, Politico, PoliticoCategoriaProjeto, DoadorPolitico
from facebook.models import FacebookProfile
from datetime import datetime


def home(request):
    facebook_profile = None
    page_render = 'home.html'
    if request.user.is_authenticated():
        facebook_profile = request.user.get_profile().get_facebook_profile()
        page_render = 'dashboard.html'

    return render(request, page_render, {'facebook_profile': facebook_profile})


def facebook_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def perfil_view(request, facebook_id):
    facebook = get_object_or_404(FacebookProfile, facebook_id=facebook_id)
    facebookdic = facebook.user.get_profile().get_facebook_profile()
    if facebookdic.get('birthday', ''):
        t1 = datetime.strptime(facebookdic['birthday'], '%m/%d/%Y')
        t2 = datetime.now()
        tdelta = t2 - t1
        yearsold = int(float(tdelta.days) / 365.242199)
    else:
        yearsold = ''
    return render(request, 'perfil.html', {
        "facebook": facebookdic,
        'yearsold': yearsold
    })


def politico_view(request, slug):
    politico = get_object_or_404(Politico, slug=slug)
    categorias = PoliticoCategoriaProjeto.objects.filter(politico=politico)
    doadores = DoadorPolitico.objects.filter(politico=politico).order_by('-valor')[:10]
    noticias = politico.noticias.all()[:20]

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
        'total_irrelevantes': total_irrelevantes,
        'doadores': doadores,
        'noticias': noticias
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
    facebook_profile = request.user.get_profile()
    politicos = []
    for acomp in Acompanhamento.objects.filter(usuario=facebook_profile).all():
        politico = acomp.politico
        politicos.append(politico)
    context = {
        'politicos_que_sigo': politicos,
    }

    return render(request, 'dashboard.html', context)


def seguir_politico(request, slug):
    try:
        politico = Politico.objects.get(slug=slug)
    except Politico.DoesNotExist:
        raise Http404

    facebook_profile = request.user.get_profile()
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
