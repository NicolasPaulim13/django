from django.shortcuts import render

def consulta(request):
    return render(request, 'consulta/consulta.html')  # Renderiza o template home.html
