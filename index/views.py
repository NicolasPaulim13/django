from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    # Lógica existente para renderizar a página inicial
    return render(request, 'index/index.html')

def logout_view(request):
    logout(request)  # Faz o logout do usuário
    return redirect('index')  # Redireciona para a página inicial após o logout
