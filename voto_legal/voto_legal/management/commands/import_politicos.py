# coding: utf-8
from django.core.management.base import BaseCommand, CommandError
from voto_legal.models import Politico, CasaGovernamental, UF, Partido
from voto_legal.util import generate_slug

from pyquery import PyQuery
import urllib
import simplexml

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        for casa in CasaGovernamental.objects.all():
            
            document = PyQuery(url="http://www.excelencias.org.br/@casa.php?pr=1&casa=%s" % casa.id_referencia)
            combo = document.find('select#escnome.casa')
            
            print("[Import Politico] - casa %s" % (casa.nome))
            
            options = combo.children()
            for i in xrange(1, len(options)):
                option = options.eq(i)[0]
                
                id_transparencia = int(option.attrib.get('value'))
                if id_transparencia > 0:
                    
                    try:
                        politico = Politico.objects.get(id_transparencia=id_transparencia)
                        
                        print("\t[Import Politico] - %s de %s, Politico ja existe %s, %s" % (i, len(options), politico.nome, politico.slug))

                    except Politico.DoesNotExist:
                        
                        try:
                            url = 'http://www.excelencias.org.br/candidato/@candidato_direta.php?id=%s' % id_transparencia
                            data = urllib.urlopen(url)
                        
                            data_content = data.read()
                            data_content = data_content.replace('&', '&amp;')
                            politico_data = simplexml.loads(data_content)
                                
                            politico_data_principal = politico_data.get('transparencia').get('parlamentar').get('principal')
                        
                            cpf = politico_data_principal.get('cpf', '').replace('.', '').replace('-', '')
                            politico = Politico.objects.create(
                                nome = politico_data_principal.get('nomeBatismo'),
                                apelido = politico_data_principal.get('apelido'),
                                slug = generate_slug(politico_data_principal.get('apelido')),
                                cpf = cpf or None,
                                partido = Partido.objects.get(sigla=politico_data_principal.get('partido', '').replace(' ', '')),
                                uf = UF.objects.get(sigla=politico_data_principal.get('uf')),
                                email = politico_data_principal.get('email', ''),
                                imagem = politico_data_principal.get('imagem'),
                                biografia = politico_data_principal.get('cargosRelevantes', ''),
                                casa_governamental = casa,
                                id_transparencia = id_transparencia
                            )

                            print("\t[Import Politico] - %s de %s, Politico criado %s, %s" % (i, len(options), politico.nome, politico.slug))

                        except Exception, e:
                            print "\t=== Oops, ocorreu um erro com a url %s: \n\t %s" % (url, e)
                            
                        
                    
                    