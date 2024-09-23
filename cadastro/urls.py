from django.urls import path
from .views import cadastro

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),  # Rota para a página de login
]
