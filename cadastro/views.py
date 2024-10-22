from django.shortcuts import render, redirect
from django.contrib import messages, auth
from cadastro_registro.models import CadastroRegistro
from django.contrib.auth.hashers import check_password

def login_page(request):
    if request.method == 'POST':
        nome_paciente = request.POST.get('nome_paciente', '').strip()
        senha_paciente = request.POST.get('senha_paciente', '').strip()

        if not nome_paciente or not senha_paciente:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'cadastro/cadastro.html')

        try:
            cadastro = CadastroRegistro.objects.get(nome_paciente=nome_paciente)

            # Verifica se a senha está correta
            if check_password(senha_paciente, cadastro.senha_paciente):
                # Autentica o usuário associado ao CadastroRegistro
                user = cadastro.user
                auth.login(request, user)  # Utiliza o sistema de autenticação do Django
                return redirect('index')
            else:
                messages.error(request, 'Senha incorreta.')
        except CadastroRegistro.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')

    return render(request, 'cadastro/cadastro.html')
