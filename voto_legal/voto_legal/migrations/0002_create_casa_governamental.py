# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from voto_legal.models import CasaGovernamental

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        
        CasaGovernamental.objects.create(id_referencia=1, nome="Câmara dos Deputados", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=2, nome="Senado Federal", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=3, nome="Assembleia Legislativa/AC", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=4, nome="Assembleia Legislativa/AM", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=5, nome="Assembleia Legislativa/AP", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=6, nome="Assembleia Legislativa/BA", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=7, nome="Assembleia Legislativa/CE", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=8, nome="Assembleia Legislativa/ES", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=9, nome="Assembleia Legislativa/GO", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=10, nome="Assembleia Legislativa/MA", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=11, nome="Assembleia Legislativa/MG", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=12, nome="Assembleia Legislativa/MS", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=13, nome="Assembleia Legislativa/MT", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=14, nome="Assembleia Legislativa/PA", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=15, nome="Assembleia Legislativa/PB", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=16, nome="Assembleia Legislativa/PE", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=17, nome="Assembleia Legislativa/PI", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=18, nome="Assembleia Legislativa/PR", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=19, nome="Assembleia Legislativa/RJ", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=20, nome="Assembleia Legislativa/RN", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=21, nome="Assembleia Legislativa/RO", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=22, nome="Assembleia Legislativa/RR", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=23, nome="Assembleia Legislativa/RS", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=24, nome="Assembleia Legislativa/SC", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=25, nome="Assembleia Legislativa/SE", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=26, nome="Assembleia Legislativa/SP", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=27, nome="Assembleia Legislativa/TO", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=28, nome="Assembleia Legislativa/AL", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=29, nome="Câmara Legislativa", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=30, nome="Câmara Municipal de São Paulo", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=31, nome="Câmara Municipal de Rio Branco", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=32, nome="Câmara Municipal de  Maceió", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=33, nome="Câmara Municipal de Manaus", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=34, nome="Câmara Municipal de Macapá", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=35, nome="Câmara Municipal de Salvador", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=36, nome="Câmara Municipal de Fortaleza", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=37, nome="Câmara Municipal de Vitória", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=38, nome="Câmara Municipal de Goiânia", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=39, nome="Câmara Municipal de São Luís", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=40, nome="Câmara Municipal de Belo Horizonte", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=41, nome="Câmara Municipal de Campo Grande", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=42, nome="Câmara Municipal de Cuiabá", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=43, nome="Câmara Municipal de Belém", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=44, nome="Câmara Municipal de João Pessoa", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=45, nome="Câmara Municipal de Recife", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=46, nome="Câmara Municipal de Teresina", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=47, nome="Câmara Municipal de Curitiba", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=48, nome="Câmara Municipal do Rio de Janeiro", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=49, nome="Câmara Municipal de Natal", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=50, nome="Câmara Municipal de Porto Velho", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=51, nome="Câmara Municipal de Boa Vista", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=52, nome="Câmara Municipal de Porto Alegre", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=53, nome="Câmara Municipal de Florianópolis", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=54, nome="Câmara Municipal de Aracaju", site="", orcamento=0, orcamento_por_habitante = 0)
        CasaGovernamental.objects.create(id_referencia=55, nome="Câmara Municipal de Palmas", site="", orcamento=0, orcamento_por_habitante = 0)
        

    def backwards(self, orm):
        CasaGovernamental.objects.delete()

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
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['voto_legal']
    symmetrical = True
