from django.urls import path
from .views import  listar_carros, detalhar_carro, realizar_aluguel, realizar_cadastro, register

urlpatterns = [
    path('carros/', listar_carros, name='listar_carros'),
    path('carros/<str:pk>', detalhar_carro, name='detalhar_carro'),
    path('aluguel/',realizar_aluguel, name='realizar_aluguel'),
    path('clientes/cadastrar',realizar_cadastro, name='realizar_cadastro'),
    path('registration', register, name= 'register'),
]