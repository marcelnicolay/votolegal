# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Politico'
        db.create_table('voto_legal_politico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('apelido', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('cpf', self.gf('django.db.models.fields.CharField')(unique=True, max_length=11)),
            ('partido', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voto_legal.Partido'])),
            ('uf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voto_legal.UF'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('imagem', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('biografia', self.gf('django.db.models.fields.TextField')()),
            ('cargo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voto_legal.Cargo'])),
            ('id_transparencia', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('voto_legal', ['Politico'])

        # Adding model 'Partido'
        db.create_table('voto_legal_partido', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sigla', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('voto_legal', ['Partido'])

        # Adding model 'CategoriaProjeto'
        db.create_table('voto_legal_categoriaprojeto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('relevante', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('voto_legal', ['CategoriaProjeto'])

        # Adding model 'CasaGovernamental'
        db.create_table('voto_legal_casagovernamental', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('orcamento', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('orcamento_por_habitante', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('id_referencia', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('voto_legal', ['CasaGovernamental'])

        # Adding model 'Doador'
        db.create_table('voto_legal_doador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cnpj_cpf', self.gf('django.db.models.fields.CharField')(max_length=14)),
        ))
        db.send_create_signal('voto_legal', ['Doador'])

        # Adding model 'DoadorPolitico'
        db.create_table('voto_legal_doadorpolitico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voto_legal.Doador'])),
            ('politico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voto_legal.Politico'])),
        ))
        db.send_create_signal('voto_legal', ['DoadorPolitico'])

        # Adding model 'UF'
        db.create_table('voto_legal_uf', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('voto_legal', ['UF'])

        # Adding model 'Cargo'
        db.create_table('voto_legal_cargo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('voto_legal', ['Cargo'])

        # Adding model 'Noticia'
        db.create_table('voto_legal_noticia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('voto_legal', ['Noticia'])

        # Adding model 'NoticiaPolitico'
        db.create_table('voto_legal_noticiapolitico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('noticia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voto_legal.Noticia'])),
            ('politico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voto_legal.Politico'])),
        ))
        db.send_create_signal('voto_legal', ['NoticiaPolitico'])


    def backwards(self, orm):
        # Deleting model 'Politico'
        db.delete_table('voto_legal_politico')

        # Deleting model 'Partido'
        db.delete_table('voto_legal_partido')

        # Deleting model 'CategoriaProjeto'
        db.delete_table('voto_legal_categoriaprojeto')

        # Deleting model 'CasaGovernamental'
        db.delete_table('voto_legal_casagovernamental')

        # Deleting model 'Doador'
        db.delete_table('voto_legal_doador')

        # Deleting model 'DoadorPolitico'
        db.delete_table('voto_legal_doadorpolitico')

        # Deleting model 'UF'
        db.delete_table('voto_legal_uf')

        # Deleting model 'Cargo'
        db.delete_table('voto_legal_cargo')

        # Deleting model 'Noticia'
        db.delete_table('voto_legal_noticia')

        # Deleting model 'NoticiaPolitico'
        db.delete_table('voto_legal_noticiapolitico')


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
            'doadores': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['voto_legal.DoadorPolitico']", 'to': "orm['voto_legal.Politico']", 'symmetrical': 'False'}),
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
            'doadores': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['voto_legal.DoadorPolitico']", 'to': "orm['voto_legal.Doador']", 'symmetrical': 'False'}),
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