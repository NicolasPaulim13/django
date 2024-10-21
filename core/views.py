from django.shortcuts import render

def faq(request):
    return render(request, 'core/faq.html')  # Renderiza o template home.html

def faq_logado(request):
    return render(request, 'core/faq_logado.html')  # Renderiza o template home.html
        