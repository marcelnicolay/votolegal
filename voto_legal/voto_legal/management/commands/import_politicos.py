from django.core.management.base import BaseCommand, CommandError
from voto_legal.models import Politico, Casa
from pyquery import PyQuery

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        for casa in Casa.objects.all():
            
            document = PyQuery(url="http://www.excelencias.org.br/@casa.php?pr=1&casa=%s" % casa.id_referencia)