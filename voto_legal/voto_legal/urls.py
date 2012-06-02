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

    # Politico template
    # Exemples:
    # politico/fulano-da-silva
    # politico/sicrano-soares
    url(r'^politico/(?P<slug>[^/]+)/?$', single_politico, name='single_politico'),

    # Politicos archive template
    url(r'^politicos?/?$', archive_politicos, name='archive_politicos'),

    # Facebook something
    url(r'^fb/', include('django_facebook.urls')),
)
