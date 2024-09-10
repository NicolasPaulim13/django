from django.shortcuts import render

def index_medico(request):
    return render(request, 'index_medico/index_medico.html')  # Renderiza o template home.html
