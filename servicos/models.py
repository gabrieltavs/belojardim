from django.db import models

# Create your models here.
class Servico(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)
    
class Atividade(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nome, self.servico.nome)
