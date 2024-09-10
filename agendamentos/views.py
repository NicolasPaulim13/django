from django.shortcuts import render, get_object_or_404, redirect
from .models import Agendamento
from .forms import AgendamentoForm

def agendamento_list(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos/agendamento_list.html', {'agendamentos': agendamentos})

def agendamento_create(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamento_list')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamentos/agendamento_form.html', {'form': form})

def agendamento_update(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('agendamento_list')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'agendamentos/agendamento_form.html', {'form': form})

def agendamento_delete(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('agendamento_list')
    return render(request, 'agendamentos/agendamento_confirm_delete.html', {'agendamento': agendamento})

