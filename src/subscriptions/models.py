from django.db import models

# Create your models here.

class Subscription(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('Email', max_length=25, blank=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)# blank= pode ser em branco
    creat_at = models.DateTimeField('Criado em ', auto_now_add=True)
    # auto_now_add = se n indicar o creat_at, ele insere a data atual
