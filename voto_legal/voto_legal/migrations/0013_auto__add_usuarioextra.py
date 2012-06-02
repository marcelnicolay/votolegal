# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UsuarioExtra'
        db.create_table('voto_legal_usuarioextra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['facebook.FacebookProfile'])),
            ('uf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voto_legal.UF'])),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voto_legal.Cidade'])),
            ('data_nascimento', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('voto_legal', ['UsuarioExtra'])


    def backwards(self, orm):
        # Deleting model 'UsuarioExtra'
        db.delete_table('voto_legal_usuarioextra')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'facebook.facebookprofile': {
            'Meta': {'object_name': 'FacebookProfile'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']", 'related_name': "'_facebook'"})
        },
        'voto_legal.acompanhamento': {
            'Meta': {'object_name': 'Acompanhamento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'politico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Politico']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facebook.FacebookProfile']"})
        },
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
            'orcamento': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '12'}),
            'orcamento_por_habitante': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '12'}),
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
            'cnpj_cpf': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'voto_legal.doadorpolitico': {
            'Meta': {'object_name': 'DoadorPolitico'},
            'doador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Doador']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'politico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Politico']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'default': 'None', 'decimal_places': '2', 'max_digits': '12'})
        },
        'voto_legal.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'unique': 'True'})
        },
        'voto_legal.noticiaacesso': {
            'Meta': {'object_name': 'NoticiaAcesso'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'facebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facebook.FacebookProfile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Noticia']"})
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
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'voto_legal.politico': {
            'Meta': {'object_name': 'Politico'},
            'apelido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'biografia': ('django.db.models.fields.TextField', [], {}),
            'cargo': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['voto_legal.Cargo']", 'default': 'None'}),
            'casa_governamental': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['voto_legal.CasaGovernamental']", 'default': 'None'}),
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '11', 'unique': 'True', 'null': 'True', 'default': 'None'}),
            'doadores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['voto_legal.Doador']", 'symmetrical': 'False', 'through': "orm['voto_legal.DoadorPolitico']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_transparencia': ('django.db.models.fields.IntegerField', [], {}),
            'imagem': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'noticias': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['voto_legal.Noticia']", 'symmetrical': 'False', 'through': "orm['voto_legal.NoticiaPolitico']"}),
            'partido': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Partido']"}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.UF']"})
        },
        'voto_legal.politicocategoriaprojeto': {
            'Meta': {'object_name': 'PoliticoCategoriaProjeto'},
            'categoria_projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.CategoriaProjeto']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'politico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Politico']"}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'voto_legal.uf': {
            'Meta': {'object_name': 'UF'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['voto_legal.Pais']", 'default': 'None'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'voto_legal.usuarioextra': {
            'Meta': {'object_name': 'UsuarioExtra'},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.Cidade']"}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voto_legal.UF']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['facebook.FacebookProfile']"})
        }
    }

    complete_apps = ['voto_legal']