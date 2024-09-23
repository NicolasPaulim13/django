from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        confirma_password = request.POST.get('confirma_password')  # Pegando o campo de confirmação de senha
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Verificar se a senha e a confirmação de senha coincidem
            if password != confirma_password:
                messages.error(request, 'As senhas não coincidem. Tente novamente.')
                return render(request, 'cadastro/cadastro.html', {'form': form})

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Seja bem-vindo(a), {username}!')
                return redirect('index_cliente')  # Redireciona para o app 'index_cliente' após login bem-sucedido
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.error(request, 'Erro ao validar o formulário.')
    else:
        form = AuthenticationForm()

    return render(request, 'cadastro/cadastro.html', {'form': form})
