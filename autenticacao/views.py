from django.shortcuts import redirect, render
from django. http import HttpResponse
from .utils import password_is_valid
# Create your views here.
def home(request):
    return redirect( 'cadastro.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('password')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/')

        return HttpResponse(f'Cadastro realizado com sucesso!!!! Olá seja bem vindo(a) {usuario}.')

        
def login(request):
    return HttpResponse("Você esta em login")