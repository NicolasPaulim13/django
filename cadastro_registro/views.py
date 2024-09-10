from django.shortcuts import render

def cadastro_registro(request):
    return render(request, 'cadastro_registro/cadastro_registro.html')  # Renderiza o template home.html
