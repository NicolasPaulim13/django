from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # Importa o decorador login_required

@login_required  # Protege a view home para que apenas usuários autenticados possam acessá-la
def consulta(request):
    return render(request, 'consulta/consulta.html')  # Renderiza o template home.html
