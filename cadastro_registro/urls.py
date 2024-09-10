# Importações necessárias para definir as rotas de URLs
from django.urls import path  # Importa a função path para definir as rotas de URL
from .views import cadastro_registro  # Importa a função de view 'home' do módulo 'views' local

# Lista de padrões de URL para a aplicação 'core'
urlpatterns = [

    path('cadastro_registro/', cadastro_registro, name='cadastro_registro'),
]
