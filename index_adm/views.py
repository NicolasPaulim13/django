from django.shortcuts import render

def index_adm(request):
    return render(request, 'index_adm/index_adm.html')  # Renderiza o template index.html
