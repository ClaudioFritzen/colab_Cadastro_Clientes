from django.shortcuts import render
from django. http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Você esta na pagina inicial")

def login(request):
    return HttpResponse("Você esta em login")