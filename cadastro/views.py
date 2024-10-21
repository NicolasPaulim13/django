from django.shortcuts import render, redirect
from django.contrib import messages
from cadastro_registro.models import CadastroRegistro
from django.contrib.auth.hashers import check_password

def login_page(request):
    if request.method == 'POST':
        nome_paciente = request.POST.get('nome_paciente', '').strip()  # Garante que seja uma string vazia se None
        senha_paciente = request.POST.get('senha_paciente', '').strip()  # Garante que seja uma string vazia se None

        print(f"Nome do paciente: {nome_paciente}")
        print(f"Senha digitada: {senha_paciente}")

        if not nome_paciente or not senha_paciente:
            print("Nome do paciente ou senha não fornecidos.")
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'cadastro/cadastro.html')

        try:
            # Verifica se o usuário existe no banco de dados CadastroRegistro
            usuario = CadastroRegistro.objects.get(nome_paciente=nome_paciente)

            print(f"Hash da senha no banco de dados: {usuario.senha_paciente}")

            # Verifica se a senha hash está correta
            if check_password(senha_paciente, usuario.senha_paciente):
                print("Senha correta, logando o usuário.")
                request.session['paciente_id'] = usuario.id  # Salva o ID do usuário na sessão
                nome = usuario.nome_paciente.split()[0]  # Pega o primeiro nome do usuário
                return redirect('index')  # Redireciona para a página após login
            else:
                print("Senha incorreta.")
                messages.error(request, 'Senha incorreta.')
        except CadastroRegistro.DoesNotExist:
            print("Usuário não encontrado.")
            messages.error(request, 'Usuário não encontrado.')

    return render(request, 'cadastro/cadastro.html')
