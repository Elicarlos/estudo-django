from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 1 aqui

def index(request):
    return HttpResponse("Ola mundo")

def home(request):
    return HttpResponse("Home")

def contato(request):
    return HttpResponse("contato")

def trabalhe(request):
    return HttpResponse("trabalhe conosco")
