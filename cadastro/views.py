from django.shortcuts import render

def cadastro(request):
    return render(request, 'cadastro/cadastro.html')  # Renderiza o template home.html
