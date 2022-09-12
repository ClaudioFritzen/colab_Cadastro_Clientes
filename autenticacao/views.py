from django.shortcuts import redirect, render
from django. http import HttpResponse
from .utils import password_is_valid
from django.contrib.auth.models import User

from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def home(request):
    return redirect('cadastro.html')

def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponse('Já está logado')
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
            messages.add_message(request, constants.SUCCESS, 'Usuário Cadastrado com sucesso' )
            return redirect('login/')
        except:
            messages.add_message(request, constants.ERRO, 'Erro interno do sistema' )
            return HttpResponse('')
        


# Autencicacao de usuario do login

def login(request):
    if request.method =="GET":
        if request.user.is_authenticated:
            return HttpResponse('Já está logado')
        return render (request, 'login.html')
    elif request.method =="POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
         
        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha está incorreta!')
            return redirect ('/login')
        else:
            auth.login(request, usuario)
            return HttpResponse('Login bem sucedido!')
            """ return redirect('/') """

# 
def sair(request):
    auth.logout(request)
    return redirect('/login')