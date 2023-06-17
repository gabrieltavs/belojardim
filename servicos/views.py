from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from .forms import FormatForm
from .admin import ServicoResource

from .models import Servico, Atividade

from django.urls import reverse_lazy

# Create your views here.
class ServicoCreate(CreateView):
    model = Servico
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servicos')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['nome', 'descricao', 'servico']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

################ UPDATE VIEW ####################

class ServicoUpdate(UpdateView):
    model = Servico
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servicos')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['nome', 'descricao', 'servico']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

################ DELETE VIEW ####################

class ServicoDelete(DeleteView):
    model = Servico
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-servicos')

class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')

################ LIST VIEW ####################

class ServicoList(ListView, FormView):
    model = Servico
    template_name = 'cadastros/listas/servico.html'
    #export json
    form_class = FormatForm

    def post(self, request, **kwargs):
        qs = self.get_queryset()
        dataset = ServicoResource().export(qs)
        
        format = request.POST.get('format')

        if format == 'xls':
            ds = dataset.xls
        elif format == 'csv':
            ds = dataset.csv
        elif format == 'json':
            ds = dataset.json

        response = HttpResponse(ds, content_type=f"{format}")
        response['Content-Disposition'] = "attachment; filename=post.{format}"
        return response




class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'