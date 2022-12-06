from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    senha = models.CharField(max_length=15)
    confirmar_senha = models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.nome
