from django.db import models

# Create your models here.

class Carro(models.Model):
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=30)
    ano = models.CharField(max_length=4)
    modelo = models.CharField(max_length=30)
    data_compra = models.DateField(max_length=8)

class Cliente(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=30)
    data_nasc = models.DateField(max_length=8)
    endereço = models.CharField(max_length=30)

class Aluguel(models.Model):
    codigo = models.CharField(max_length=30)  
    data_aluguel = models.DateField(max_length=8)  
    data_entrega = models.DateField(max_length=8)
    diaria = models.CharField(max_length=30)