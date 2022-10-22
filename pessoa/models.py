from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True )

    def __str__(self) -> str:
        return self.nome_completo

class Animal(models.Model):
    nome = models.CharField(max_length=256)
    tipo = models.CharField(max_length=256)
    vacina = models.BooleanField(default=False)
    descricao = models.CharField(max_length=256)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome