from django.shortcuts import render, redirect
from django.contrib import messages
from cadastro_registro.models import CadastroRegistro  # Importa o modelo CadastroRegistro do app correspondente

def login_page(request):
    if request.method == 'POST':
        nome_paciente = request.POST.get('nome_paciente')
        senha_paciente = request.POST.get('senha_paciente')
        confirma_senha_paciente = request.POST.get('confirma_senha_paciente')

        # Verifica se a senha e a confirmação de senha coincidem
        if senha_paciente != confirma_senha_paciente:
            messages.error(request, 'As senhas não coincidem. Tente novamente.')
            return render(request, 'cadastro/cadastro.html')

        try:
            # Verifica se o usuário existe no banco de dados CadastroRegistro
            usuario = CadastroRegistro.objects.get(nome_paciente=nome_paciente)

            # Verifica se a senha está correta
            if usuario.senha_paciente == senha_paciente:
                nome = usuario.nome_paciente.split()[0]  # Pega o primeiro nome do usuário
                return render(request, 'index_cliente.html', {'nomes': [nome]})
            else:
                messages.error(request, 'Senha incorreta.')
        except CadastroRegistro.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')

    return render(request, 'cadastro/cadastro.html')
