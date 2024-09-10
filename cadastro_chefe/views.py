from django.shortcuts import render

def cadastro_chefe(request):
    return render(request, 'cadastro_chefe/cadastro_chefe.html')  # Renderiza o template home.html
