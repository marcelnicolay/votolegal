import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from voto_legal.models import Politico


def home(request):
    facebook_profile = None
    if request.user.is_authenticated():
        facebook_profile = request.user.get_profile().get_facebook_profile()
    return render(request, 'home.html', {'facebook_profile': facebook_profile})


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def single_politico(request, slug):
    return render(request, 'single-politico.html', {
        'politico_slug': slug
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
