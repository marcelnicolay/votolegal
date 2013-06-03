import json
from datetime import datetime, date

from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django_facebook.models import FacebookCustomUser

from voto_legal.models import (Acompanhamento, FacebookProfileManager, Politico,
    PoliticoCategoriaProjeto, DoadorPolitico, NoticiaAcesso, Noticia, UF, UsuarioExtra)


def home(request):
    if request.user.is_authenticated():
        page_render = 'dashboard.html'
        user = request.user

        try:
            usuario_dados = UsuarioExtra.objects.get(user=user)
        except UsuarioExtra.DoesNotExist:
            usuario_dados = None

        politicos = []
        for acomp in Acompanhamento.objects.filter(usuario=user).all():
            politico = acomp.politico
            politicos.append(politico)

        fb_profile_manager = FacebookProfileManager(user)
        my_friends = fb_profile_manager.get_app_friends()

        context = {
            'politicos_que_sigo': politicos,
            'my_friends': my_friends,
            'usuario_dados': usuario_dados,
            'estados': UF.objects.all()
        }
    else:
        page_render = 'home.html'
        context = {}

    return render(request, page_render, context)


def facebook_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def perfil_view(request, facebook_id):
    fb_user = get_object_or_404(FacebookCustomUser, facebook_id=facebook_id)

    if fb_user.date_of_birth:
        t2 = date.today()
        tdelta = t2 - fb_user.date_of_birth
        yearsold = int(float(tdelta.days) / 365.242199)
    else:
        yearsold = ''

    politicos = []
    for acomp in Acompanhamento.objects.filter(usuario=fb_user).all():
        politico = acomp.politico
        politicos.append(politico)

    return render(request, 'perfil.html', {
        "fb_user": fb_user,
        'yearsold': yearsold,
        'politicos_que_sigo': politicos,
    })


def politico_view(request, slug):
    politico = get_object_or_404(Politico, slug=slug)
    categorias = PoliticoCategoriaProjeto.objects.filter(politico=politico)
    doadores = DoadorPolitico.objects.filter(politico=politico).order_by('-valor')[:10]
    noticias = politico.noticias.all()[:20]

    user = request.user
    acompanhamento = None
    if not user.is_anonymous():
        acompanhamento = Acompanhamento.objects.filter(usuario=user, politico=politico)

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
        'noticias': noticias,
        'acompanhamento': acompanhamento
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


def ver_noticia(request, id):
    noticia = Noticia.objects.get(pk=id)
    acessos, _ = NoticiaAcesso.objects.get_or_create(noticia=noticia, facebook=request.user)
    acessos.count += 1
    acessos.save()

    return HttpResponseRedirect(noticia.url)


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


def usuario_estado(request):
    estado = UF.objects.get(id=request.GET.get('estado'))

    usuario_extra, _ = UsuarioExtra.objects.get_or_create(user=request.user)
    usuario_extra.uf = estado
    usuario_extra.save()

    context = {
        'politicos': [p.as_dict() for p in usuario_extra.politico_same_uf]
    }

    return HttpResponse(json.dumps(context), mimetype='application/json')


def esquecer_politico(request, slug):
    try:
        politico = Politico.objects.get(slug=slug)
    except Politico.DoesNotExist:
        raise Http404

    politico.esquecer(request.user)
    context = {
        'status': 'ok',
    }

    return HttpResponse(json.dumps(context), mimetype='application/json')


def politicos_que_sigo(request):
    if not request.user.is_authenticated():
        raise Http404

    politicos = []
    for acomp in Acompanhamento.objects.filter(user=request.user).all():
        politico = acomp.politico
        politicos.append({
            'nome': politico.nome,
            'slug': politico.slug,
        })

    context = {
        'politicos': politicos,
    }

    return HttpResponse(json.dumps(context), mimetype='application/json')
