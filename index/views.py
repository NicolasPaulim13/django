from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html')  # Renderiza o template home.html


