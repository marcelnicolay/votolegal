from django.conf.urls import patterns, include, url
from django.contrib import admin
from voto_legal.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voto_legal.views.home', name='home'),
    # url(r'^voto_legal/', include('voto_legal.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Home template
    url(r'^$', home, name='home'),

    # Register template
    url(r'^registrar/?$', register, name='register'),

    # Login template
    url(r'^logar/?$', login, name='login'),

    url(r'^dashboard/?$', dashboard, name="dashboard"),

    url(r'^politico/(?P<slug>[^/]+)/?$', politico_view, name='single_politico'),
    url(r'^politico/(?P<slug>[^/]+)/seguir/?$', seguir_politico, name='seguir_politico'),
    url(r'^politicos/follow/?$', politicos_que_sigo, name="politicos_que_sigo"),

    # Politicos archive template
    url(r'^politicos?/?$', archive_politicos, name='archive_politicos'),

    url(r'^ajax/politicos/(?P<nome>[^/]+)/?$', ajax_politicos, name="ajax_politicos"),

    # Facebook
    url(r'^facebook/login$', 'facebook.views.login', name='facebook_login'),
    url(r'^facebook/authentication_callback$', 'facebook.views.callback', name='facebook-callback'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
)
