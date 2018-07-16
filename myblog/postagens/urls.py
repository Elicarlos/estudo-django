from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes', views.detalhes, name='detalhes'),
    path('contatos', views.contatos,  name='contatos')

]
