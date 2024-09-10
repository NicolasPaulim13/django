from django.shortcuts import render

def index_cliente(request):
    return render(request, 'index_cliente/index_cliente.html')  # Renderiza o template home.html
