# coding: utf-8
import urllib
#from bs4 import BeautifulSoup
from pyquery import PyQuery
from django.core.management.base import BaseCommand

from voto_legal.models import CasaGovernamental


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for casa in CasaGovernamental.objects.all():
            self._parse_politicos_projetos(casa.id)

    def _parse_politicos_projetos(casa_id):
        url = "http://www.excelencias.org.br/@pls.php?cs={0}".format(casa_id)
        document = PyQuery(url=url)
        doc = document.find('#restringe').eq(1).find('tr')

        politicos = {}
        last_name = None
        abort_user = False
        for i in xrange(0, len(doc)):
            elem = doc.eq(i)
            nome = elem.find('td b a').html()
            if nome:
                politicos[nome] = {}
                last_name = nome
                abort_user = False
                continue
            # Ainda não chegou nas células com os dados
            if last_name is None:
                continue
            if abort_user:
                continue

            titulo_categoria = elem.find('td i')
            if titulo_categoria.html() == "Categoria":
                categ_lines = titulo_categoria.parents('tr').eq(0).nextAll('tr')
                for j in xrange(0, len(categ_lines)):
                    categ_base = categ_lines.eq(j).children('td')
                    # Chegamos na linha antes da do total, aborta e passa pro
                    # próximo usuário
                    if categ_base.eq(0).html() and categ_base.eq(0).html().strip() == "" and not categ_base.eq(1).html():
                        abort_user = True
                        break
                    categ_titulo = categ_base.eq(0).html()
                    categ_valor_a = categ_base.eq(1).html()
                    categ_valor_b = categ_base.eq(2).html()
                    politicos[last_name][categ_titulo] = {
                        'sem_relevancia': categ_valor_a.strip(),
                        'outros': categ_valor_b.strip(),
                    }
                    #print "%s: %s / %s" % (last_name, repr(categ_titulo), repr(categ_valor_b))
                if abort_user:
                    continue
        return politicos

