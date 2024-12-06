from django.shortcuts import render
from django.http import HttpResponse
from .models import Modelo

# Create your views here.


def home(request):
    texto = Modelo(name="Ambiente configurado")
    mensagem = f"texto normal: {texto.name}"
    mensagemAlterada = f"texto em Maiúsculo: {texto.uppercase_name()}"
    return HttpResponse(mensagem + "<br>" + mensagemAlterada)
