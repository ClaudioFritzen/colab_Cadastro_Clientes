from django.shortcuts import redirect, render
from django. http import HttpResponse
from .utils import password_is_valid, email_html
from django.contrib.auth.models import User

from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

# importando as configurações do settings para chamada do token de ativação
import os
from django.conf import settings

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponse('Já está logado {{usuario}}')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('password')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/')
        
        try:
            user = User.objects.create_user(username=usuario, password=senha, is_active=False)
            user.save()

            # apos salvar enviar o email de usuario
            path_template = os.path.join(settings.BASE_DIR,'autenticacao/templates/emails/cadastro_confirmado.html')
            email_html(path_template, 'Cadastro confirmado', [email,], username=usuario) #link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}")
            messages.add_message(request, constants.SUCCESS, 'Usuário Cadastrado com sucesso' )
            return redirect('login/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema' )
            return redirect('/')
        


# Autencicacao de usuario do login

def login(request):
    if request.method =="GET":
        if request.user.is_authenticated:
            return HttpResponse('Já está logado {{username}}')
        return render (request, 'login.html')
    elif request.method =="POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
         
        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/login')
        else:
            auth.login(request, usuario)
            return redirect('/pagefinal.html')

# 
def sair(request):
    auth.logout(request)
    return redirect('/login')