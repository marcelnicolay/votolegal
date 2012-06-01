# coding: utf-8
from django.db import models


class Politico(models.Model):
    nome = models.CharField(max_length=150)
    apelido = models.CharField(max_length=100)
    slug = models.SlugField()
    cpf = models.CharField(max_length=11, unique=True)
    partido = models.ForeignKey('Partido')
    uf = models.ForeignKey('UF')
    email = models.EmailField()
    imagem = models.URLField()
    site = models.URLField()
    biografia = models.TextField()
    doadores = models.ManyToManyField('Doador', through='DoadorPolitico')
    cargo = models.ForeignKey('Cargo')
    id_transparencia = models.IntegerField()


class Partido(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, unique=True)
    site = models.URLField()


class CategoriaProjeto(models.Model):
    nome = models.CharField(max_length=100)
    relevante = models.BooleanField()


class CasaGovernamental(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField()
    site = models.URLField()
    orcamento = models.DecimalField(max_digits=12, decimal_places=2)
    orcamento_por_habitante = models.DecimalField(max_digits=12, decimal_places=2)
    id_referencia = models.IntegerField()


class Doador(models.Model):
    nome = models.CharField(max_length=50)
    cnpj_cpf = models.CharField(max_length=14)
    doadores = models.ManyToManyField('Politico', through='DoadorPolitico')


class DoadorPolitico(models.Model):
    doador = models.ForeignKey(Doador)
    politico = models.ForeignKey(Politico)


class Pais(models.Model):
    nome = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nome


class UF(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais, default=None, null=True)


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(UF)


class Cargo(models.Model):
    nome = models.CharField(max_length=50)


class Noticia(models.Model):
    titulo = models.CharField(max_length=250)
    url = models.URLField(unique=True)


class NoticiaPolitico(models.Model):
    noticia = models.ForeignKey(Noticia)
    politico = models.ForeignKey(Politico)
