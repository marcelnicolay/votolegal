from django.core.management.base import BaseCommand, CommandError
from voto_legal.models import Partido
from voto_legal.util import generate_slug

from pyquery import PyQuery

import urllib
import simplexml

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        document = PyQuery(url="http://www.tse.jus.br/partidos/partidos-politicos")
        trs = document.find('div#portal-conteudo').find('table.grid tbody tr')
        
        for i in xrange(1, len(trs)-1):
            
            tds = trs.eq(i).find('td')
            
            sigla = tds.eq(1).children().children().text()
            nome = tds.eq(2).text().capitalize()
            
            print '[Import Partidos][%s] - Get or update partido [%s,%s] ' % (i, nome, sigla)
            
            partido, created = Partido.objects.get_or_create(
                sigla=sigla,
                nome=nome
            )            
    
            