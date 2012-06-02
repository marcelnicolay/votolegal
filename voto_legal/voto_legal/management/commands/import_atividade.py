# coding: utf-8
import re

from pyquery import PyQuery
from django.core.management.base import BaseCommand

from voto_legal.models import (CasaGovernamental, CategoriaProjeto, Politico,
    PoliticoCategoriaProjeto)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for casa in CasaGovernamental.objects.all():
            print u"Importando dados de {0}".format(casa.nome)
            self._parse_politicos_projetos(casa.id_referencia)

    def _parse_politicos_projetos(self, casa_id):
        url = "http://www.excelencias.org.br/@pls.php?cs={0}".format(casa_id)
        document = PyQuery(url=url)
        doc = document.find('#restringe').eq(1).find('tr')
        # javascript:lpls(8362,'QWJlbGFyZG8gQ2FtYXJpbmhh',1)
        link_regex = re.compile('javascript\:lpls\((\d+),')

        politicos = {}
        last_name = None
        last_id_referencia = None
        abort_user = False
        for i in xrange(0, len(doc)):
            elem = doc.eq(i)
            nome = elem.find('td b a').html()
            if nome:
                politicos[nome] = {}
                last_name = nome
                link = elem.find('td b a')[0].attrib.get('href')
                found = link_regex.match(link)
                last_id_referencia = int(found.group(1))
                abort_user = False
                continue
            # Ainda não chegou nas células com os dados
            if last_name is None:
                continue
            if abort_user:
                continue

            print u"\tImportando dados do politico {0} ({1})".format(last_name, last_id_referencia)
            try:
                politico = Politico.objects.get(id_transparencia=last_id_referencia)
            except Politico.DoesNotExist:
                print u"\tPolítico {0} ({1}) não existe".format(last_name, last_id_referencia)
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
                    categ_valor_a = categ_base.eq(1).html().strip() or 0
                    categ_valor_b = categ_base.eq(2).html().strip() or 0
                    politicos[last_name][categ_titulo] = {
                        'sem_relevancia': categ_valor_a,
                        'outros': categ_valor_b,
                    }
                    # É uma categoria relevante
                    if categ_valor_b:
                        relevante = True
                        valor = categ_valor_b
                    else:
                        relevante = False
                        valor = categ_valor_a
                    categoria_projeto, _ = CategoriaProjeto.objects.get_or_create(nome=categ_titulo, relevante=relevante)

                    pcp, _ = PoliticoCategoriaProjeto.objects.get_or_create(politico=politico, categoria_projeto=categoria_projeto)
                    pcp.quantidade = valor
                    pcp.save()
                    print u"\t\t{0}: {1} / {2}".format(categ_titulo, categ_valor_a, categ_valor_b)
                if abort_user:
                    continue
        return politicos
