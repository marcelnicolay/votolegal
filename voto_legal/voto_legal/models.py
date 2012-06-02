# coding: utf-8
from django.db import models
from facebook.models import FacebookProfile


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


class Acompanhamento(models.Model):
    usuario = models.ForeignKey(FacebookProfile)
    politico = models.ForeignKey(Politico)
