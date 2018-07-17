from django.shortcuts import render
from django.template import loader
from django.http import Http404
from .models import Pergunta

# Create your views here.
# 1 aqui

def index(request):
    latest_question_list = Pergunta.objects.order_by('-data_publicacao')[:5]
    template = loader.get_template('postagens/index.html')
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'postagens/index.html', context)

# ...
def detalhes(request, pergunta):
    try:
        pergunta = Pergunta.objects.get(pk=pergunta)
    except Pergunta.DoesNotExist:
        raise Http404("A pergunta nao existe")
    return render(request, 'postagens/detalhes.html', { 'pergunta' : pergunta})

def resultados(request):
    response = "Voce esta vendo os resultados da pesquisa %s ."
    return HttpResponse(response % pergunta)

def votos(request):
    return HttpResponse("Voce esta votando %s ." %pergunta)
