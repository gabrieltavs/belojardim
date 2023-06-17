from django.urls import path

from .views import ServicoCreate, AtividadeCreate
from .views import ServicoUpdate, AtividadeUpdate
from .views import ServicoDelete, AtividadeDelete
from .views import ServicoList, AtividadeList

urlpatterns = [
    path('cadastrar/servico/', ServicoCreate.as_view(), name="cadastrar-servico"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),


    path('editar/servico/<int:pk>/', ServicoUpdate.as_view(), name="editar-servico"),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name="editar-atividade"),


    path('excluir/servico/<int:pk>/', ServicoDelete.as_view(), name="excluir-servico"),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name="excluir-atividade"),

    path('listar/servicos/', ServicoList.as_view(), name="listar-servicos"),
    path('listar/atividades/', AtividadeList.as_view(), name="listar-atividades"),
]
