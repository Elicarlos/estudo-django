from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('contato', views.contato, name='contato'),
    path('trabalhe', views.trabalhe, name='trabalhe-conosco')
]
