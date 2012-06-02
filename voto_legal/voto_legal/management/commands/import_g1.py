# coding: utf-8
import time
import urllib

from pyquery import PyQuery
from django.core.management.base import BaseCommand

from voto_legal.models import Noticia, NoticiaPolitico, Politico


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # rodrigo maia = 429
        #politico = Politico.objects.get(pk=429)
        for politico in Politico.objects.all():
            print u"Importando notícias sobre {0}".format(politico.apelido)
            self._import(politico, 1)
            self._import(politico, 2)
            time.sleep(5)

    def _import(self, politico, pagina=1):
        nome = urllib.quote_plus(politico.apelido.encode('utf8'))
        url = u'http://busca.globo.com/Busca/g1/?query=%22{nome}%22&ordenacao=descending&offset={pagina}&xargs=&formato=&requisitor=g1&aba=todos&filtro=subeditorias%3A%5EPol%C3%ADtica%24&on=false&formatos=1296%2C1285%2C1%2C10%2C0%2C0%2C0%2C0%2C0%2C0%2C0&filtroData=&dataA=&dataB='.format(nome=nome, pagina=pagina)
        document = PyQuery(url=url)
        resultados = document.find("#lista-de-resultados dt a")
        for i in xrange(0, len(resultados)):
            elem = resultados.eq(i)
            titulo = elem.text().encode('latin1').decode('utf8')
            url = elem[0].attrib.get('href')

            print u"Noticia {0} <{1}>".format(titulo, url)

            noticia, _ = Noticia.objects.get_or_create(titulo=titulo, url=url)
            NoticiaPolitico.objects.get_or_create(noticia=noticia, politico=politico)
