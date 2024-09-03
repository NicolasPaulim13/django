from django.shortcuts import render

def cadastro_adm(request):
    return render(request, 'cadastro_adm/cadastro_adm.html')  # Renderiza o template home.html
