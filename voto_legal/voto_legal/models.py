# coding: utf-8
import json
import urllib

from django.db import models
from facebook import models as fb_models


class Politico(models.Model):
    nome = models.CharField(max_length=150)
    apelido = models.CharField(max_length=100)
    slug = models.SlugField()
    cpf = models.CharField(max_length=11, unique=True, null=True, default=None)
    partido = models.ForeignKey('Partido')
    uf = models.ForeignKey('UF')
    email = models.EmailField()
    imagem = models.URLField()
    site = models.URLField()
    biografia = models.TextField()
    doadores = models.ManyToManyField('Doador', through='DoadorPolitico')
    cargo = models.ForeignKey('Cargo', null=True, default=None)
    casa_governamental = models.ForeignKey('CasaGovernamental', null=True, default=None)
    id_transparencia = models.IntegerField()

    noticias = models.ManyToManyField('Noticia', through='NoticiaPolitico')

    def __unicode__(self):
        return "%s (%s-%s)" % (self.apelido, self.partido.sigla, self.uf.sigla)

    def seguir(self, usuario):
        Acompanhamento.objects.get_or_create(politico=self, usuario=usuario)

    def esquecer(self, usuario):
        Acompanhamento.objects.filter(politico=self, usuario=usuario).delete()

class Partido(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, unique=True)
    site = models.URLField()

    def __unicode__(self):
        return self.nome

class CategoriaProjeto(models.Model):
    nome = models.CharField(max_length=100)
    relevante = models.BooleanField()

    def __unicode__(self):
        return self.nome


class PoliticoCategoriaProjeto(models.Model):
    politico = models.ForeignKey(Politico)
    categoria_projeto = models.ForeignKey(CategoriaProjeto)
    quantidade = models.IntegerField(default=0)


class CasaGovernamental(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField()
    site = models.URLField()
    orcamento = models.DecimalField(max_digits=12, decimal_places=2)
    orcamento_por_habitante = models.DecimalField(max_digits=12, decimal_places=2)
    id_referencia = models.IntegerField()
    def __unicode__(self):
        return self.nome


class Doador(models.Model):
    nome = models.CharField(max_length=250)
    cnpj_cpf = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.nome

class DoadorPolitico(models.Model):
    doador = models.ForeignKey(Doador)
    politico = models.ForeignKey(Politico)
    valor = models.DecimalField(max_digits=12, decimal_places=2, default=None, null=True)

class Pais(models.Model):
    nome = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nome


class UF(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais, default=None, null=True)

    def __unicode__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(UF)

    def __unicode__(self):
        return self.nome


class Cargo(models.Model):
    nome = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=250)
    url = models.URLField(unique=True)


class NoticiaPolitico(models.Model):
    noticia = models.ForeignKey(Noticia)
    politico = models.ForeignKey(Politico)


class NoticiaAcesso(models.Model):
    noticia = models.ForeignKey(Noticia)
    facebook = models.ForeignKey(fb_models.FacebookProfile)
    count = models.IntegerField(default=0)


class UsuarioExtra(models.Model):
    user = models.OneToOneField(fb_models.FacebookProfile)
    uf = models.ForeignKey(UF)
    cidade = models.ForeignKey(Cidade)
    data_nascimento = models.DateField()


class FacebookProfileManager(object):
    def __init__(self, facebook_profile):
        self.facebook_profile = facebook_profile

    def get_app_friends(self):
        obj = self.facebook_profile
        my_friends_ids = []

        url = "https://graph.facebook.com/{fb_id}/friends?access_token={token}".format(fb_id=obj.facebook_id, token=obj.access_token)
        url_data = urllib.urlopen(url).read()
        friends_list = json.loads(url_data)
        for friend in friends_list.get('data', []):
            my_friends_ids.append(int(friend['id']))

        # TODO: pegar outras paginas
        #while friends_list.get('paging', dict()).get('next'):
        #    next_page = friends_list.get('paging', dict()).get('next')
        #    url_data = urllib.urlopen(url).read()
        #    friends_list = json.loads(url_data)
        #    for friend in friends_list.get('data', []):
        #        my_friends_ids.append(int(friend['id']))


        my_friends = fb_models.FacebookProfile.objects.filter(facebook_id__in=my_friends_ids)
        response = []
        for friend in my_friends.all():
            data = friend.get_facebook_profile()
            response.append({
                'fb_id': data['id'],
                'name': data['name'],
                'username': data['username'],
                'picture': data['picture'],
            })
        return response


class Acompanhamento(models.Model):
    usuario = models.ForeignKey(fb_models.FacebookProfile)
    politico = models.ForeignKey(Politico)
