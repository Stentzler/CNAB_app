from django.db import models
import uuid


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    tipo = models.CharField(max_length=1)
    data = models.CharField(max_length=15)
    valor = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=15)
    hora = models.CharField(max_length=15)
    dono_da_loja = models.CharField(max_length=16)
    nome_da_loja = models.CharField(max_length=21)
