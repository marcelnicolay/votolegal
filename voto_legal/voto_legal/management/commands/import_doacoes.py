# coding: utf-8
import urllib
import re

from decimal import Decimal
from pyquery import PyQuery
from django.core.management.base import BaseCommand
from BeautifulSoup import BeautifulSoup
from voto_legal.models import CasaGovernamental, Politico, Doador, DoadorPolitico

class Command(BaseCommand):

    base_url = "http://www.asclaras.org.br"
    
    def handle(self, *args, **kwargs):
        
        has_candidadato = True
        offset = 0
        
        while has_candidadato:
            
            url = self.base_url + '/partes/index/candidatos_frame.php?CAoffset=%s' % offset
            print "=== " + url
            
            document = PyQuery(url=url)
            trs = document.find('tr')
            
            for i in xrange(1, len(trs) -1):
                td = trs.eq(i).find('td')
                
                try:
                    politico_nome = td.eq(0).children().html()
                    politico_uf = td.eq(5).html()
                    politico_url = re.search(r"(?P<url>\/[^/]+)\'", td.eq(0).children()[0].attrib.get('href')).groupdict().get('url')
                    
                    politico = Politico.objects.get(nome__iexact=politico_nome, uf__sigla=politico_uf)
                    
                    if DoadorPolitico.objects.filter(politico=politico).exists():
                        print "\tpolitico já processado %s " % politico
                        continue
                    
                    print "\t------ " + (self.base_url+politico_url)
                    soup = BeautifulSoup(urllib.urlopen(self.base_url+politico_url).read())
                    doadores_tds = soup.findAll('td', attrs={'class': re.compile('linhas2?')})
                    
                    if doadores_tds:
                        print "\tpolitico encontrado %s " % politico
                        
                        for step in xrange(0, len(doadores_tds), 3):
                            if not doadores_tds[step] or not doadores_tds[step].a:
                                continue
                                
                            doador_nome = doadores_tds[step].a.getText()
                            doador_id = doadores_tds[step+1].getText()
                            doador_valor = doadores_tds[step+2].getText()
                        
                            if not doador_id:
                                continue
                                
                            try:
                                doador = Doador.objects.get(cnpj_cpf = doador_id)
                            except Doador.DoesNotExist:
                                doador = Doador.objects.create(nome = doador_nome.replace('\t', '').capitalize(), cnpj_cpf = doador_id)
                                print "\tcriando doador %s" % doador

                            doadorPolitico, _ = DoadorPolitico.objects.get_or_create(politico=politico, doador=doador)
                        
                            found = re.search(r'(?P<inteiro>\d.*)\,\d{2}$', doador_valor)
                            if found:
                                doador_valor = found.groupdict().get('inteiro', 0)
                            else:
                                doador_valor = re.search(r'[\d\,\.]+', doador_valor).group(0)
                                
                            doadorPolitico.valor = Decimal(doador_valor.replace('.', '').replace(',', ''))
                            doadorPolitico.save()
                    
                except Politico.DoesNotExist:
                    #print "Politico nao existe %s " % politico_nome
                    pass
            
            offset += 20