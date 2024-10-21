from django.contrib import admin
from .models import Consulta

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'assunto', 'data', 'horario')
    search_fields = ('nome', 'email', 'telefone')
    list_filter = ('data', 'horario')
    ordering = ('data', 'horario')

admin.site.register(Consulta, ConsultaAdmin)
