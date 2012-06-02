# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from voto_legal.models import Pais, UF, Cidade

import os

class Migration(DataMigration):
    def forwards(self, orm):
        dump_data = open(os.path.join(os.path.dirname(__file__), 'municipios.sql'), 'r')
        db.execute(dump_data.read())

    def backwards(self, orm):
        brasil = Pais.objects.get(nome='Brasil')
        estados_brasileiros = UF.objects.filter(pais=brasil)
        cidades_brasileiras = Cidade.objects.filter(estado__in=estados_brasileiros)
        cidades_brasileiras.delete()
        estados_brasileiros.delete()
        brasil.delete()

    models = {
        'voto_legal.cargo': {
            'Meta': {'object_name': 'Cargo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'voto_legal.casagovernamental': {
            'Meta': {'object_name': 'CasaGovernamental'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_referencia': ('django.db.models.fields.IntegerField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'orcamento': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'orcamento_por_habitante': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'voto_legal.categoriaprojeto': {
            'Meta': {'object_name': 'CategoriaProjeto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'relevante': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'voto_legal.cidade': {
            'Meta': {'object_name': 'Cidade'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.UF']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'voto_legal.doador': {
            'Meta': {'object_name': 'Doador'},
            'cnpj_cpf': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'doadores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['voto_legal.Politico']", 'through': "orm['voto_legal.DoadorPolitico']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'voto_legal.doadorpolitico': {
            'Meta': {'object_name': 'DoadorPolitico'},
            'doador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Doador']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'politico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Politico']"})
        },
        'voto_legal.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        },
        'voto_legal.noticiapolitico': {
            'Meta': {'object_name': 'NoticiaPolitico'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Noticia']"}),
            'politico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Politico']"})
        },
        'voto_legal.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'voto_legal.partido': {
            'Meta': {'object_name': 'Partido'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sigla': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'voto_legal.politico': {
            'Meta': {'object_name': 'Politico'},
            'apelido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'biografia': ('django.db.models.fields.TextField', [], {}),
            'cargo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Cargo']"}),
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'doadores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['voto_legal.Doador']", 'through': "orm['voto_legal.DoadorPolitico']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_transparencia': ('django.db.models.fields.IntegerField', [], {}),
            'imagem': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'partido': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Partido']"}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.UF']"})
        },
        'voto_legal.uf': {
            'Meta': {'object_name': 'UF'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['voto_legal.Pais']", 'null': 'True'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['voto_legal']
    symmetrical = True
