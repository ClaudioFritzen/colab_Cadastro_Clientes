from django.shortcuts import render
from django. http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        return HttpResponse("Testando")
        
def login(request):
    return HttpResponse("Você esta em login")