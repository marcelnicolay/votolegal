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
            
            for option in combo.children():
                id_transparencia = int(option.attrib.get('value'))
                if id_transparencia > 0:
                    
                    data = urllib.urlopen('http://www.excelencias.org.br/candidato/@candidato_direta.php?id=%s' % id_transparencia)
                    politico_data = simplexml.loads(data.read())
                    politico_data_principal = politico_data.get('transparencia').get('parlamentar').get('principal')
                    
                    if not Politico.objects.filter(id_transparencia=id_transparencia).exists():
                        politico = Politico.objects.get_or_create(
                            nome = politico_data_principal.get('nomeBatismo'),
                            apelido = politico_data_principal.get('apelido'),
                            slug = generate_slug(politico_data_principal.get('apelido')),
                            cpf = politico_data_principal.get('cpf'),
                            partido = Partido.objects.get_or_create(sigla=politico_data_principal.get('partido')),
                            uf = UF.objects.get(sigla=politico_data_principal.get('sigla')),
                            email = politico_data_principal.get('email'),
                            imagem = politico_data_principal.get('imagem'),
                            biografia = politico_data_principal.get('cargosRelevantes'),
                            id_transparencia = id_transparencia
                        )
                    
                    