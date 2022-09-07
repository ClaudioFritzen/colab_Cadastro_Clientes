from pydoc import render_doc
from django.shortcuts import render
from django. http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('password')
        return HttpResponse(f'Cadastro realizado com sucesso!!!!'
            'Olá seja bem vindo(a) {usuario}. Seu email é {email} {senha} {confirmar_senha}')
            
        
def login(request):
    return HttpResponse("Você esta em login")