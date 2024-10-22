from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def consulta(request):
    # Lógica da consulta aqui...
    return render(request, 'consulta/consulta.html')

