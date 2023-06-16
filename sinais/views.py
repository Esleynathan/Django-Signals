from django.shortcuts import render
from . models import Pessoa

def home(request):
    x = Pessoa(nome='Ésle Nathan', email='esley@e.com', telefone='21990238348')
    x.save()
    return HttpReponse('Olá')