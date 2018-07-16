import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Pergunta(models.Model):
    pergunta_texto = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('Data Publicada')
    def __str__(self):
        return self.pergunta_texto

class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    escolha_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.pergunta
    def __str__(self):
        return self.escolha_texto
        
    def  publicado_em(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
