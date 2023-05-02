from django.forms import forms
from .models import Carro, Cliente, Aluguel
class CarroForm(forms.Form):
   class Meta:
      form = Carro
      fields = ['placa, marca, ano, modelo, data_compra']


class ClienteForm(forms.Form):
   class Meta:
      form = Cliente
      fields = ['cpf, nome, data_nasc, endereço']


class AluguelForm(forms.Form):
   class Meta:
      form = Aluguel
      fields = ['codigo, data_aluguel, data_entrega, diaria']