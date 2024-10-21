from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import CadastroRegistroForm

# Função para renderizar o formulário de registro
def cadastro_registro(request):
    form = CadastroRegistroForm()
    return render(request, 'cadastro_registro/cadastro_registro.html', {'form': form})

# Função para criar um novo paciente
def cadastro_create_paciente(request):
    if request.method == 'POST':
        form = CadastroRegistroForm(request.POST)
        
        if form.is_valid():
            # Cria o usuário primeiro
            username = form.cleaned_data['email_paciente']  # Usando email como username
            senha = form.cleaned_data['senha_paciente']
            user = User.objects.create(username=username, password=make_password(senha))
            
            # Associa o cadastro ao usuário criado
            form.save(user=user)
            
            return redirect('login')  # Redireciona para a página de login após o cadastro
    else:
        form = CadastroRegistroForm()

    return render(request, 'cadastro_registro/cadastro_registro.html', {'form': form})
