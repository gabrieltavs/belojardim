from django.contrib import admin
from .models import Servico, Atividade
from import_export import resources

# Register your models here.

class ServicoResource(resources.ModelResource):
    class Meta:
        model = Servico
        fields = ('nome', 'descricao')


admin.site.register(Servico)
admin.site.register(Atividade)