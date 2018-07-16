from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Pergunta
from django.http import HttpResponse

# Create your views here.
# 1 aqui

def index(request):
    return render(request, 'postagens/index.html')


# ...
def detalhes(request):
    return render(request, 'postagens/detalhes.html')

def contatos(request):
    return render(request, 'postagens/contatos.html')
