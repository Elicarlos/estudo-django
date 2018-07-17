from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pergunta>/detalhes/', views.detalhes, name='detalhes'),
    path('<int:pergunta>/resultados/', views.resultados, name='resultados'),
    path('<int:pergunta>/votos/', views.votos, name="votos"),

]
