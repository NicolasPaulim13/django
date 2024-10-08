from django.shortcuts import render

def planos(request):
    return render(request, 'planos/planos.html')  # Renderiza o template home.html

def planos_logado(request):
    return render(request, 'planos_logado/planos_logado.html')  # Renderiza o template home.html
