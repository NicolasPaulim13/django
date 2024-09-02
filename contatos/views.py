from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # Importa o decorador login_required

@login_required  # Protege a view home para que apenas usuários autenticados possam acessá-la
def contatos(request):
    return render(request, 'contatos/contatos.html')  # Renderiza o template home.html
