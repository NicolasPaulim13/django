from django.shortcuts import render, redirect
from .forms import CadastroRegistroForm

def cadastro_registro(request):
    form = CadastroRegistroForm()
    return render(request, 'cadastro_registro/cadastro_registro.html', {'form': form})

def cadastro_create_paciente(request):
    if request.method == 'POST':
        form = CadastroRegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return redirect('cadastro')  # Redireciona para a página de login após o cadastro
    else:
        form = CadastroRegistroForm()
    return render(request, 'cadastro_registro/cadastro_registro.html', {'form': form})
