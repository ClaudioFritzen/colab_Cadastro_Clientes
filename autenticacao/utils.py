import re
from django.contrib import messages
from django.contrib.messages import constants

def password_is_valid(request, senha, confirmar_senha):
    if len(senha) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve ter no minimo seis digitos')
        return False
    
    if not senha == confirmar_senha:
        messages.add_message(request, constants.ERROR, 'As senhas não são iguais')
    
    # validações de caracteres

    if not re.search('[A-Z]', senha):
        messages.add_message(request, constants.ERROR, 'Está faltando uma letra Maiuscula')
        return False
    
    if not re.search('[a-z]', senha):
        messages.add_message(request, constants.ERROR, 'sua senha tem que ter uma letra minuscula')
        return False
    
    if not re.search('[1-9]', senha):
        messages.add_message(request, constants.ERROR, 'Senha deve conter um número')
        return False
        
    return True
