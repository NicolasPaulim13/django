from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # Importa o decorador login_required

@login_required  # Protege a view home para que apenas usuários autenticados possam acessá-la
def planos(request):
    return render(request, 'planos/planos.html')  # Renderiza o template home.html
