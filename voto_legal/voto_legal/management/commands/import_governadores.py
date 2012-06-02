# coding: utf-8
import urllib
import re

from decimal import Decimal
from pyquery import PyQuery
from django.core.management.base import BaseCommand
from BeautifulSoup import BeautifulSoup
from voto_legal.models import CasaGovernamental, Politico, Doador, DoadorPolitico, Partido, UF

from voto_legal.util import generate_slug
import os

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        path = os.path.join(os.path.dirname(__file__), '../../migrations/governadores.html')
        document = PyQuery(open(path, 'r').read())
        
        trs = document.find('.sortable.wikitable').eq(0).children()
        
        for i in xrange(1, len(trs)):
            tr = trs.eq(i)
            estado = tr.children().eq(0).children().children().html()
            nome = tr.children().eq(1).children().html()
            
            imagem = ''
            if tr.children().eq(2).children():
                imagem = "http://" +  PyQuery(tr.children().eq(2).children().html()).attr('src').replace('45px', '116px')
                
            partido = tr.children().eq(3).children().html()
            
            politico = Politico.objects.create(
                nome = nome,
                apelido = nome,
                slug = generate_slug(nome),
                cpf = None,
                partido = Partido.objects.get(sigla=partido),
                uf = UF.objects.get(nome=estado),
                email = '',
                imagem = imagem,
                biografia = '',
                id_transparencia = -1
            )
