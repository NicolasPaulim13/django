from django.shortcuts import render, redirect
from .forms import ConsultaForm

def marcar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return redirect('consulta_sucesso')  # Redireciona para uma página de sucesso
    else:
        form = ConsultaForm()
    
    return render(request, 'marcar_consulta.html', {'form': form})
