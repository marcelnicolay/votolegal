# coding: utf-8
from django.contrib import admin
from voto_legal.models import (Cargo, Doador, Partido, Politico, CasaGovernamental)


admin.site.register(Cargo)
admin.site.register(Doador)
admin.site.register(Partido)
admin.site.register(Politico)
admin.site.register(CasaGovernamental)
