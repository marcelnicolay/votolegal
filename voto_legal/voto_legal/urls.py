from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Logout redirect
    url(r'^logout$', 'voto_legal.views.facebook_logout', name='facebook_logout'),

    # Home template
    url(r'^$', 'voto_legal.views.home', name='home'),

    # Perfil de usuario template
    # Exemples:
    # perfil/fulano-da-silva
    # perfil/sicrano-soares
    url(r'^perfil/(?P<facebook_id>[^/]+)/?$', 'voto_legal.views.perfil_view', name='perfil'),

    url(r'^usuario/estado?$', 'voto_legal.views.usuario_estado', name='usuario_estado'),

    # Politico template
    # Exemples:
    # politico/fulano-da-silva
    # politico/sicrano-soares
    url(r'^politico/(?P<slug>[^/]+)/?$', 'voto_legal.views.politico_view', name='single_politico'),
    url(r'^politico/(?P<slug>[^/]+)/seguir/?$', 'voto_legal.views.seguir_politico', name='seguir_politico'),
    url(r'^politico/(?P<slug>[^/]+)/esquecer/?$', 'voto_legal.views.esquecer_politico', name='esquecer_politico'),
    url(r'^politicos/follow/?$', 'voto_legal.views.politicos_que_sigo', name="politicos_que_sigo"),

    # Redirect Noticia template
    # Exemples:
    # ver/1429
    # ver/1044
    url(r'^ver/(?P<id>[^/]+)/?$', 'voto_legal.views.ver_noticia', name='ver_noticia'),

    # Politicos archive template
    url(r'^politicos?/?$', 'voto_legal.views.archive_politicos', name='archive_politicos'),

    url(r'^ajax/politicos/(?P<nome>[^/]+)/?$', 'voto_legal.views.ajax_politicos', name="ajax_politicos"),

    (r'^facebook/', include('django_facebook.urls')),
)

urlpatterns += staticfiles_urlpatterns()
